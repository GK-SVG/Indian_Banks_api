from django.urls import path
from .views import (
    BankListAPIView
)
    
    
urlpatterns = [
    path('',BankListAPIView.as_view(),name='PostListAPIView'),
]

