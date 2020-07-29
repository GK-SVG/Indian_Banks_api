from django.urls import path
from .views import (
    PersonListAPIView,
    PersonCreate,
    PersonDeleteAPIView,
    PersonUpdateAPIView
)
urlpatterns = [
    path('',PersonListAPIView.as_view(),name='PersonListAPIView'),
    path('edit/<int:id>/',PersonUpdateAPIView.as_view(),name='Update'),
    path('delete/<int:id>/',PersonDeleteAPIView.as_view(),name='Delete'),
    path('create/',PersonCreate.as_view(),name='Create'),
]
