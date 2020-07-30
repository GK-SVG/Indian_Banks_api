from django.urls import path
from .views import *
urlpatterns = [
    path('person/',PersonListAPIView.as_view(),name='PersonListAPIView'),
    path('person/edit/<int:id>/',PersonUpdateAPIView.as_view(),name='PersonUpdateAPIView'),
    path('person/delete/<int:id>/',PersonDeleteAPIView.as_view(),name='PersonDeleteAPIView'),
    path('person/create/',PersonCreate.as_view(),name='PersonCreate'),
    path('country/',CountryListAPIView.as_view(),name='CountryListAPIView'),
    path('country/edit/<int:id>/',CountryUpdateAPIView.as_view(),name='CountryUpdateAPIView'),
    path('country/delete/<int:id>/',CountryDeleteAPIView.as_view(),name='CountryDeleteAPIView'),
    path('country/create/',CountryCreate.as_view(),name='CountryCreate'),
    path('state/',StateListAPIView.as_view(),name='StateListAPIView'),
    path('state/edit/<int:id>/',StateUpdateAPIView.as_view(),name='StateUpdateAPIView'),
    path('state/delete/<int:id>/',StateDeleteAPIView.as_view(),name='StateDeleteAPIView'),
    path('state/create/',StateCreate.as_view(),name='StateCreate'),
    path('city/',CityListAPIView.as_view(),name='CityListAPIView'),
    path('city/edit/<int:id>/',CityUpdateAPIView.as_view(),name='CityUpdateAPIView'),
    path('city/delete/<int:id>/',CityDeleteAPIView.as_view(),name='CityDeleteAPIView'),
    path('city/create/',CityCreate.as_view(),name='CityCreate'),
    path('town/',TownListAPIView.as_view(),name='TownListAPIView'),
    path('town/edit/<int:id>/',TownUpdateAPIView.as_view(),name='TownUpdateAPIView'),
    path('town/delete/<int:id>/',TownDeleteAPIView.as_view(),name='TownDeleteAPIView'),
    path('town/create/',TownCreate.as_view(),name='TownCreate'),
]
