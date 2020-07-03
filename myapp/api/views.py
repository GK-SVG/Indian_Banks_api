from rest_framework.generics import ListAPIView
from .serializers import BankSerializer
from myapp.models import BankDetail
from rest_framework import filters


class BankListAPIView(ListAPIView):
    search_fields = ['ifsc','city','bank_name','state']
    filter_backends = (filters.SearchFilter,)
    queryset=BankDetail.objects.all()
    serializer_class=BankSerializer

