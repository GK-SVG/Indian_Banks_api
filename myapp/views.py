from django.shortcuts import render
from .models import BankDetail

def home(request):
    return render(request,'base.html')

def search_ifsc(request):
    ifsc=request.GET.get('ifsc')
    print('ifsc==',ifsc)
    banks=BankDetail.objects.filter(ifsc=ifsc)
    print('Bank==',banks)
    return render(request,'search2.html',{'banks':banks})

def search_dist(request):
    city=request.GET.get('city')
    bank=request.GET.get('bank')
    banks=BankDetail.objects.filter(city=city.upper(),bank_name=bank.upper())
    return render(request,'search.html',{'banks':banks})