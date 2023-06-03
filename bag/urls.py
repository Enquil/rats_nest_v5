from django.urls import path
from . import views

urlpatterns = [
    path('', views.BagView.as_view(), name="shopping_bag"),
    path('add/<item_id>', views.AddItem.as_view(), name="add_item"),
]
