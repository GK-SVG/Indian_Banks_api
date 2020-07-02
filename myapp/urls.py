from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('search_ifsc',views.search_ifsc,name='search_ifsc'),
    path('searchDist',views.search_dist,name='search_dist'),
]
