from django.urls import path
from .views import (
    QuestionAnswerListAPIView
)
    
    
urlpatterns = [
    path('',QuestionAnswerListAPIView.as_view(),name='QuestionAnswerListAPIView'),
]

