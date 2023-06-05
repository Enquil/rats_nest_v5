from django.urls import path
from . import views

urlpatterns = [
    path('', views.SiteManager.as_view(), name='site_manager'),
]
