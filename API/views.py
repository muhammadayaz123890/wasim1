from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from .models import *
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password, make_password
from .serializers import ProductSerializer,SellerProfileSerializer
from authsuper import views
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.views.decorators.csrf import csrf_exempt
User = get_user_model()

from rest_framework.views import APIView

class SellerProfileCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SellerProfile.objects.all()
    serializer_class = SellerProfileSerializer

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        # Debugging: Print request data
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            print("Serializer is valid")
        else:
            print("Serializer errors:", serializer.errors)
        return super().create(request, *args, **kwargs)




@csrf_exempt
def CreateProduct(request):

    message = None

    user = request.user

    if request.method == 'POST':

        message = "Someone made a Post request to create a product"

        title = request.POST.get('title')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        desc = request.POST.get('desc')

        try:
            new_product = Product.objects.create(
                user=user,
                title=title,
                category=category,
                quantity=quantity,
                price=price,
                desc=desc
            )

            new_product.save()

            message = "success"
            return response(response.status_int)
        except Exception as e:
            message = 'Error'


    response = JsonResponse({'message': message})
    response["Access-Control-Allow-Origin"] = "http://localhost:3000"
    response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"

    return response



########################################    CREATE PRODUCT VIEW               ################################




from rest_framework import viewsets

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        user = request.user
        seller_profiles = SellerProfile.objects.filter(user=user)
        if seller_profiles.exists():
            queryset = Product.objects.filter(user=user)
            serializer = ProductSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({'detail': 'Seller profile not found'}, status=status.HTTP_305_USE_PROXY)

    elif request.method == 'POST':
        user = request.user
        seller_profiles = SellerProfile.objects.filter(user=user)
        if user and seller_profiles.exists():
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Seller profile not found'}, status=status.HTTP_305_USE_PROXY)




class ProductUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()


class SellerProfileRetrieveView(generics.RetrieveAPIView):
    serializer_class = SellerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):

        user = self.request.user
        profile = get_object_or_404(SellerProfile, user=user)

        return profile

class SellerProfileCreateView(generics.CreateAPIView):
    serializer_class = SellerProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)
