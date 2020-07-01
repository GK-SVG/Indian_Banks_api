from rest_framework.generics import ListAPIView
from .serializers import BankSerializer
from myapp.models import BankDetail
class BankListAPIView(ListAPIView):
    queryset=BankDetail.objects.all()
    serializer_class=BankSerializer