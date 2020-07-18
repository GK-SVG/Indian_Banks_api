from django.shortcuts import render,HttpResponse
from .models import QuestionAnswer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from algebraAPI.api.serializers import QuestionAnswerSerializer

def home(request):
    return render(request,'algebra.html')
    
def create_question(request):
    question=request.GET.get('query')
    answer=QuestionAnswer.objects.filter(question=question)
    if answer:
        serializer=QuestionAnswerSerializer(answer,many=True)
        return JsonResponse(serializer.data,status=200,safe=False)
    else:
        return HttpResponse('Question Not abalable Please contact for this question')

