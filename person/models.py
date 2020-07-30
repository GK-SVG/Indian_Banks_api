from django.db import models

    
class Country(models.Model):
    country=models.CharField(max_length=50,unique=True)
    description=models.TextField(max_length=300)
    population=models.IntegerField()
    gdp=models.FloatField()

    def __str__(self):
        return self.country
    

class State(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    state=models.CharField(max_length=50,unique=True)
    description=models.TextField(max_length=300)
    population=models.IntegerField()
    gdp=models.FloatField()

    def __str__(self):
        return self.state

class City(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    city=models.CharField(max_length=50,unique=True)
    description=models.TextField(max_length=300)
    population=models.IntegerField()
    gdp=models.FloatField()
    pincode=models.CharField(max_length=10)
    def __str__(self):
        return self.city

class Town(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    town=models.CharField(max_length=50,unique=True)
    description=models.TextField(max_length=300)
    population=models.IntegerField()
    gdp=models.FloatField()
    pincode=models.CharField(max_length=10)
    def __str__(self):
        return self.town

class Person(models.Model):
    person_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default='')
    county=models.ForeignKey(Country,default='',on_delete=models.CASCADE)
    state=models.ForeignKey(State,default='',on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
