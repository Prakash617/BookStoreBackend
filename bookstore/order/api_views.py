from rest_framework import viewsets
from .models import *
from .serializers import *
from django.db import transaction
from product.models import *
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from .utils import *
from rest_framework.permissions import AllowAny


class OrderQuantityViewSet(viewsets.ModelViewSet):
    queryset = OrderQuantity.objects.all()
    serializer_class = OrderQuantitySerializer


class CustomerAddressViewSet(viewsets.ModelViewSet):
    
    queryset = CustomerAddress.objects.all()
    serializer_class=CustomerAddressSerializer
    permission_classes = [AllowAny]


class GuestOrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            with transaction.atomic():
                subtotal = 0
                order_items_data = data.get('order_qty', [])
                product_quantities = []


                # Calculate subtotal and create product quantity data
                for item_data in order_items_data:
                    product = item_data['product']
                    quantity = item_data['quantity']
                    price = Book.objects.get(id=product).price
                    subtotal += quantity * price

                    # Create product quantity data
                    product_quantity = OrderQuantity(product=Book.objects.get(id=product), quantity=quantity, initial_price=price)
                    product_quantity.save()
                    product_quantities.append(product_quantity)
                print("product_quantities",product_quantities)

                # Calculate discount
                print("subtotal",subtotal)
                
                coupon_code = data.get('coupon', None)
                
                if coupon_code:
                    try:
                        coupon = Coupon.objects.get(name=coupon_code)
                        discount = apply_coupon_discount(coupon,subtotal)
                        c_name = coupon.name
                    except Coupon.DoesNotExist:
                        discount = 0
                        coupon = None
                        c_name = None
                        
                else:
                    discount = 0
                    coupon = None
                    c_name = None
                print("discount",discount)
                total_price_after_discount = subtotal - discount
                tax = data.get('tax', None)
                if tax:
                    tax_value = (total_price_after_discount * tax)/100
                    price_after_tax = total_price_after_discount + tax_value
                else:
                    price_after_tax = total_price_after_discount
                    tax_value = 0
                print("tax_value",tax_value)
                shipping_charge = data.get('shipping_charge', None)
                if shipping_charge:
                    if coupon:
                        if coupon.coupon_types == "Free Shiping":
                            shipping_charge = 0
                    grannd_total = price_after_tax + shipping_charge
                else:
                    grannd_total = price_after_tax
                print("grannd_total",grannd_total)
                
                # Create or link the customer
                customer_address_data = data.get('customer_address', {})

                customer_email = customer_address_data['email']
                phone = customer_address_data['phone']
                try:
                    user = CustomUser.objects.get(email=customer_email)
                    user.phone=phone
                    user.save()
                except:
                    # Create a new user with a complex password
                    password = generate_complex_password()
                    user = CustomUser(username=customer_email,email=customer_email, password=password,phone=phone)
                    user.save()
                    


                 # Link or create customer address
                

                matching_address = CustomerAddress.objects.filter(
                        Q(full_name=customer_address_data['full_name']) &
                        Q(email=customer_address_data['email']) &
                        Q(phone=customer_address_data['phone']) &
                        Q(address_line_1=customer_address_data['address_line_1']) &
                        Q(address_line_2=customer_address_data['address_line_2']) &
                        Q(city=customer_address_data['city']) &
                        Q(country=customer_address_data['country']) 
                       
                    )
                
                if matching_address.exists():
                        customer_address = matching_address.first()
                else:
                    customer_address = CustomerAddress(**customer_address_data,customer=user)
                    customer_address.save()
                
                # Create payment details
                payment_details = PaymentDetail(amount=grannd_total)
                payment_details.save()


                # Create order object
                order = Orders(
                    initial_price=subtotal,
                    amount_to_pay=grannd_total,
                    tax=tax_value,
                    discount=discount,
                    shipping_charge=data.get('shipping_charge',0),
                    customer=user,
                    address=customer_address,
                    payment_details=payment_details,
                    coupon = c_name


                )
                order.save()
                payment_details.order_id = order.uuid
               
                # Attach product quantities to the order
                for i in product_quantities:
                    order.order_qty.add(i)

                order.save()
                for item_data in order_items_data:
                    product = item_data['product']
                    quantity = item_data['quantity']
                    book = Book.objects.get(id=product)
                    book.sell_quantity += quantity
                    book.save()


                serializer = self.get_serializer(order)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class OrderRejectedViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    http_method_names = ['put']
    serializer_class = OrderSerializer
    lookup_field = 'uuid'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = 'Rejected'
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
class OrderCancelledViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]
    http_method_names = ['put']
    lookup_field = 'uuid'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = 'Cancelled'
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class OrdersTrackingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

    def list(self, request):
        email = request.query_params.get('email')
        print(email)

        if not email:
            return Response({'error': 'Email parameter is missing'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = CustomUser.objects.get(email=email)
            print(user)
            orders = Orders.objects.filter(customer=user).last()
            serializer = self.get_serializer(orders, many=False)
            return Response(serializer.data)

        except:
            return Response({'error': 'Email address is not match'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        