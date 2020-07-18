from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('answer/',views.create_question,name='create_question')
]
