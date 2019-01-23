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
from rest_framework import generics, permissions
from django.core.exceptions import ObjectDoesNotExist

class users(generics.ListCreateAPIView):
    queryset = PhonitaurUser.objects.all()
    serializer_class = PhonitaurUserSerializer
    permission_classes = ()

class oneUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhonitaurUser.objects.all()
    serializer_class = PhonitaurUserSerializer
    permission_classes = ()

class languages(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = ()

class oneLanguage(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = ()

def languageByName(request, lang):
    if request.method == 'GET':
        lessonList = Language.objects.filter(name = lang)
        serializer = LanguageSerializer(lessonList, many=True)
        return JsonResponse(serializer.data, safe=False)

class questions(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = ()

class allLessons(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = ()

def lessons(request, lang):
    if request.method == 'GET':
        lessonList = Lesson.objects.filter(language = lang)
        serializer = LessonSerializer(lessonList, many=True)
        return JsonResponse(serializer.data, safe=False)

class oneLesson(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = ()
