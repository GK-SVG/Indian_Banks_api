from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
    path('api/',include('myapp.api.urls')),
    path('algebra/',include('algebraAPI.urls')),
    path('algebraApi/',include('algebraAPI.api.urls')),
    path('personApi/',include('person.api.urls')),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

