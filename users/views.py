from django.shortcuts import render

from .models import User, Language, Lesson, Question
from .serializers import UserSerializer, LanguageSerializer, LessonSerializer, QuestionSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

def index(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

def oneUser(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

def languages(request):
    if request.method == 'GET':
        languageList = Language.objects.all()
        serializer = LanguageSerializer(languageList, many=True)
        return JsonResponse(serializer.data, safe=False)

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
