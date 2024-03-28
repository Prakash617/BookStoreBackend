from django.shortcuts import HttpResponse, render, HttpResponse,redirect
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import *
from rest_framework.decorators import action
from django.http import HttpResponseRedirect
from django.urls import reverse
from .utils import send_verify_email,send_resetpassword_link
from bookstore.settings import ip



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
    'refresh': str(refresh),
    'access': str(refresh.access_token),
    }




class UserRegister(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]
    def create(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        email = user.username
        print(email)
        link = f"{ip}/api/user/verify?uuid={user.uuid}"
        print(link)
        send_verify_email(link= link, email =email,username=user.full_name)
        return Response({'token':token, 'msg':'Registration Successful', 'uuid': user.uuid}, status=status.HTTP_201_CREATED)


class UserLoginViewSet(viewsets.ModelViewSet):
    
    queryset = CustomUser.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    
    def list(self, request, *args, **kwargs):
        return Response({"error":"login_required"})
    

    def create(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        
        # username = serializer.data.get('username')
        # password = serializer.data.get('password')
        # user = authenticate(username=username, password=password)
        # if user is not None:
        token = get_tokens_for_user(user)
        return Response({'token':token, 'msg':f'Login Success', 'uuid': user.uuid}, status=status.HTTP_200_OK)
        # else:
            # return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)


class MyDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CustomUserListSerializer
    permission_classes = [IsAuthenticated]
    

    def get_queryset(self):
        return CustomUser.objects.filter(pk=self.request.user.pk)



class UserVerificationViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]


    def list(self, request):
        id = request.GET.get('uuid', None)
        if id:
            try:
                user = CustomUser.objects.get(uuid= id)
                user.isEmailVerified = True
                user.save()
                return redirect('http://127.0.0.1:8000/api/')
               
            except CustomUser.DoesNotExist:
                return Response({'message': 'User not found'})
        else:
            return Response({'message': 'Please provide an user id'})
            




class UserChangePasswordViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ['patch']
    permission_classes = [IsAuthenticated]


    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            old_password = serializer.validated_data.get("old_password")
            new_password = serializer.validated_data.get("new_password")

            # Check if old password is correct
            if not user.check_password(old_password):
                return Response({"detail": "Old password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)

            # Set new password and save
            user.set_password(new_password)
            user.save()
            return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordLinkViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['POST'], url_path='api/user/reset_password_link')
    def forgot_password(self, request):
        serializer = ForgotPasswordLinkSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return Response({"detail": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)

            # Generate and send reset password link via email
            # You need to implement the email sending logic here
            reset_password_link = f"{ip}/api/user/reset-password/?token={user.uuid}&email={user.email}/"
            
            send_resetpassword_link(link= reset_password_link, email =email)

            return Response({"detail": "Password reset link sent successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
