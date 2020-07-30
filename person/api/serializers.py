from rest_framework.serializers import ModelSerializer
from person.models import (Person,
     City,
     Country,
     Town,
     State 
)

class PersonSerializer(ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'

class CountrySerializer(ModelSerializer):
    class Meta:
        model=Country
        fields='__all__'

class StateSerializer(ModelSerializer):
    class Meta:
        model=State
        fields='__all__'

class CitySerializer(ModelSerializer):
    class Meta:
        model=City
        fields='__all__'

class TownSerializer(ModelSerializer):
    class Meta:
        model=Town
        fields='__all__'