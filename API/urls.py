from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import product_list,ProductDeleteView,ProductUpdateView,SellerProfileCreateView,SellerProfileRetrieveView, SellerProfileCreateAPIView

urlpatterns = [
    path('creation/', product_list),
    path('product-delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('products/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('seller-profile/', SellerProfileRetrieveView.as_view(), name='seller-profile-retrieve'),
    path('create-seller-profile/',  SellerProfileCreateAPIView.as_view(), name='create-seller-profile'),

]
