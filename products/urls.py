from django.urls import path
from . import views

urlpatterns = [
    path('<str:param>', views.ProductView.as_view(), name='products'),
]
