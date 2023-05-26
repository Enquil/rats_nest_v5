from django.urls import path
from . import views

urlpatterns = [
    path('products', views.HomeView.as_view(), name="index"),
]
