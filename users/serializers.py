from rest_framework import serializers
from .models import PhonitaurUser, Language, Lesson, Question

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

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields=('id', 'name', 'language', 'icon', 'level')

    def create(self, validated_data):
        return Lesson.objects.create(validated_data)

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields=('id', 'question_text', 'lesson', 'answer')

    def create(self, validated_data):
        return Question.objects.create(validated_data)
