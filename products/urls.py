from django.urls import path
from . import views

urlpatterns = [
    path('<str:category>', views.ProductView.as_view(), name='products'),
]
