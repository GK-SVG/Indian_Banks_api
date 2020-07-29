from rest_framework.generics import (ListAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView)
from .serializers import PersonSerializer
from person.models import Person
from rest_framework import filters


class PersonListAPIView(ListAPIView):
    search_fields = ['country','state','city']
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