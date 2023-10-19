from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from .serializers import LoginSerializer,RegistrationSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from API.models import Product
from .serializers import ProductSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class LoginView(APIView):
    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']


        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'detail': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            if User.objects.filter(username=username).exists():
                return Response({'message': 'Username or email already in use'}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]  # Use TokenAuthentication
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # Filter products to show only those created by the logged-in user
        return Product.objects.filter(user=self.request.user)
