from rest_framework.generics import ListAPIView
from .serializers import QuestionAnswerSerializer
from algebraAPI.models import QuestionAnswer
from rest_framework import filters


class QuestionAnswerListAPIView(ListAPIView):
    search_fields = ['question']
    filter_backends = (filters.SearchFilter,)
    queryset=QuestionAnswer.objects.all()
    serializer_class=QuestionAnswerSerializer

