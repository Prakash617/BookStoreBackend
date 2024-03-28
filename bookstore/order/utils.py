def generate_complex_password():
        # Implement your password generation logic here
        import random
        import string

        length = random.randint(7, 10)
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))


def apply_coupon_discount(coupon, order_total):
        if coupon.coupon_types == 'Flat Discount':
            discount_amount = coupon.coupon_details.get('discountAmount', 0)
        elif coupon.coupon_types == 'Percentage Discount':
            discount_percent = coupon.coupon_details.get('discountAmount', 0)
            discount_amount = (int(order_total) * int(discount_percent)) / 100
            print(discount_amount)
        else:
            discount_amount = 0
        
        return discount_amount
