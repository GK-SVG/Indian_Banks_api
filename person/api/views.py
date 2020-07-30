from rest_framework.generics import (ListAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView)
from .serializers import (PersonSerializer,
     CountrySerializer,
     StateSerializer,
     CitySerializer,
     TownSerializer
)
from person.models import (Person,
     Country,
     State,
     City,
     Town
)
from rest_framework import filters


class PersonListAPIView(ListAPIView):
    search_fields = ['id','name','country','state']
    filter_backends = (filters.SearchFilter,)
    queryset=Person.objects.all()
    serializer_class=PersonSerializer

class PersonCreate(ListCreateAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer

class PersonDeleteAPIView(DestroyAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    lookup_field='id'

class PersonUpdateAPIView(UpdateAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    lookup_field='id'

class CountryListAPIView(ListAPIView):
    search_fields = ['id','country']
    filter_backends = (filters.SearchFilter,)
    queryset=Country.objects.all()
    serializer_class=CountrySerializer

class CountryCreate(ListCreateAPIView):
    queryset=Country.objects.all()
    serializer_class=CountrySerializer

class CountryDeleteAPIView(DestroyAPIView):
    queryset=Country.objects.all()
    serializer_class=CountrySerializer
    lookup_field='id'

class CountryUpdateAPIView(UpdateAPIView):
    queryset=Country.objects.all()
    serializer_class=CountrySerializer
    lookup_field='id'

class StateListAPIView(ListAPIView):
    search_fields = ['id','country','state']
    filter_backends = (filters.SearchFilter,)
    queryset=State.objects.all()
    serializer_class=StateSerializer

class StateCreate(ListCreateAPIView):
    queryset=State.objects.all()
    serializer_class=StateSerializer

class StateDeleteAPIView(DestroyAPIView):
    queryset=State.objects.all()
    serializer_class=StateSerializer
    lookup_field='id'

class StateUpdateAPIView(UpdateAPIView):
    queryset=State.objects.all()
    serializer_class=StateSerializer
    lookup_field='id'

class CityListAPIView(ListAPIView):
    search_fields = ['id','country','state','city']
    filter_backends = (filters.SearchFilter,)
    queryset=City.objects.all()
    serializer_class=CitySerializer

class CityCreate(ListCreateAPIView):
    queryset=City.objects.all()
    serializer_class=CitySerializer

class CityDeleteAPIView(DestroyAPIView):
    queryset=City.objects.all()
    serializer_class=CitySerializer
    lookup_field='id'

class CityUpdateAPIView(UpdateAPIView):
    queryset=City.objects.all()
    serializer_class=CitySerializer
    lookup_field='id'

class TownListAPIView(ListAPIView):
    search_fields = ['id','country','state','town']
    filter_backends = (filters.SearchFilter,)
    queryset=Town.objects.all()
    serializer_class=TownSerializer

class TownCreate(ListCreateAPIView):
    queryset=Town.objects.all()
    serializer_class=TownSerializer

class TownDeleteAPIView(DestroyAPIView):
    queryset=Town.objects.all()
    serializer_class=TownSerializer
    lookup_field='id'

class TownUpdateAPIView(UpdateAPIView):
    queryset=Town.objects.all()
    serializer_class=TownSerializer
    lookup_field='id'