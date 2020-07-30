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

class TownSerializer(ModelSerializer):
    class Meta:
        model=Town
        fields=['town','description','population','gdp','pincode']

class CitySerializer(ModelSerializer):
    class Meta:
        model=City
        fields=['city','description','population','gdp','pincode']

class StateSerializer(ModelSerializer):
    town=TownSerializer(many=True)
    city=CitySerializer(many=True)
    class Meta:
        model=State
        fields=['state','description','population','gdp','city','town']

class CountrySerializer(ModelSerializer):
    states=StateSerializer(many=True)
    class Meta:
        model=Country
        fields=['country', 'description', 'population','gdp','states']



