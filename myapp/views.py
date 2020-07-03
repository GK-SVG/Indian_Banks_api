from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import BankDetail
from myapp.api.serializers import BankSerializer
from rest_framework.response import Response
from django.http import JsonResponse

def home(request):
    return render(request,'base.html')

@api_view(['GET'])
def search_ifsc(request):
    ifsc=request.GET.get('ifsc')
    banks=BankDetail.objects.filter(ifsc=ifsc)
    serializer=BankSerializer(banks,many=True)
    return Response(serializer.data,status=200)


@api_view(['GET'])
def search_dist(request):
    city=request.GET.get('city')
    bank=request.GET.get('bank')
    banks=BankDetail.objects.filter(city=city.upper(),bank_name=bank.upper())
    serializer=BankSerializer(banks,many=True)
    return Response(serializer.data,status=200)