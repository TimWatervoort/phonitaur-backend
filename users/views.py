from django.shortcuts import render

from .models import PhonitaurUser, Language, Lesson, Question
from .serializers import PhonitaurUserSerializer, LanguageSerializer, LessonSerializer, QuestionSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
import json

@api_view(['GET', 'POST'])
def index(request, format=None):
    if request.method == 'GET':
        users = PhonitaurUser.objects.all()
        serializer = PhonitaurUserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        newBody = request.body.decode('utf-8')
        jsonBody = json.loads(newBody)
        serializer = PhonitaurUserSerializer(data=jsonBody)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def oneUser(request, pk):
    try:
        user = PhonitaurUser.objects.get(pk=pk)
    except PhonitaurUser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PhonitaurUserSerializer(user)
        return JsonResponse(serializer.data)

def languages(request):
    if request.method == 'GET':
        languageList = Language.objects.all()
        serializer = LanguageSerializer(languageList, many=True)
        return JsonResponse(serializer.data, safe=False)

def oneAlphabet(request, pk):
    try:
        language = Language.objects.get(pk=pk)
    except Language.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LanguageSerializer(language)
        return JsonResponse(serializer.data)

def lessons(request, lang_id):
    if request.method == 'GET':
        lessonList = Lesson.objects.filter(language = lang_id)
        serializer = LessonSerializer(lessonList, many=True)
        return JsonResponse(serializer.data, safe=False)

def lesson(request, lesson_id):
    if request.method == 'GET':
        questionList = Question.objects.filter(lesson = lesson_id)
        serializer = QuestionSerializer(questionList, many=True)
        return JsonResponse(serializer.data, safe=False)
