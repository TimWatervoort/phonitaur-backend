from rest_framework import serializers
from .models import PhonitaurUser, Language, Lesson, Question
import json

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields=('id', 'name', 'img', 'text_color')

    def create(self, validated_data):
        return Language.objects.create(validated_data)

class PhonitaurUserSerializer(serializers.ModelSerializer):

    languages=LanguageSerializer(many=True, required=False, read_only=False)

    class Meta:
        model = PhonitaurUser
        fields=('id', 'username', 'password', 'email', 'mother_alphabet', 'img', 'languages')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True},
            'img': {'required': False}
        }


    def create(self, validated_data):
        instance = PhonitaurUser.objects.create(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            mother_alphabet=validated_data['mother_alphabet']
        )
        instance.set_password(validated_data['password'].strip())
        instance.save()
        return instance

    def update(self, instance, validated_data):

        if 'languages' in validated_data:
            languages = []
            for i in validated_data['languages']:
                newi = json.loads(json.dumps(i))
                lang = Language.objects.get(name = newi['name'])
                languages = languages + [lang]

        if 'img' in validated_data:
            instance.img = validated_data['img']

        instance.languages.set(languages)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.mother_alphabet = validated_data.get('mother_alphabet', instance.mother_alphabet)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields=('id', 'question_text', 'answer')

    def create(self, validated_data):
        return Question.objects.create(validated_data)

class LessonSerializer(serializers.ModelSerializer):

    questions=QuestionSerializer(many=True, required=False, read_only=False)

    class Meta:
        model = Lesson
        fields=('id', 'name', 'language', 'lesson_text', 'icon', 'level', 'questions')

    def create(self, validated_data):
        return Lesson.objects.create(validated_data)
