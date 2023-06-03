from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductView.as_view(), name='products'),
    path('<product_sku>', views.ProductDetail.as_view(),
         name='product_detail'),
]
