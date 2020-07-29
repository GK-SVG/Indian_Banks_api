from django.contrib import admin
from .models import Person,Country,State,City,Town
# Register your models here.
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Town)
admin.site.register(Person)
