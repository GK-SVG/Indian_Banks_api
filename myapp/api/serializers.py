from rest_framework.serializers import ModelSerializer
from myapp.models import BankDetail

class BankSerializer(ModelSerializer):
    class Meta:
        model=BankDetail
        fields=[
            'ifsc',
            'bank_id',
            'branch',
            'address',
            'city',
            'district',
            'state',
            'bank_name',
        ]