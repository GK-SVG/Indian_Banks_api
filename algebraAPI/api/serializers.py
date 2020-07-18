from rest_framework.serializers import ModelSerializer
from algebraAPI.models import QuestionAnswer

class QuestionAnswerSerializer(ModelSerializer):
    class Meta:
        model=QuestionAnswer
        fields='__all__'