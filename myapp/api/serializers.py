from rest_framework.serializers import ModelSerializer
from myapp.models import BankDetail

class BankSerializer(ModelSerializer):
    class Meta:
        model=BankDetail
        fields='__all__'