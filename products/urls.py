from django.urls import path
from . import views

urlpatterns = [
    path('<str:query>', views.ProductView.as_view(), name='products'),
]
