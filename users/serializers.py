from rest_framework import serializers
from .models import User, Language, Lesson

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields=('id', 'name', 'img', 'text_color')

    def create(self, validated_data):
        return Language.objects.create(validated_data)

class UserSerializer(serializers.ModelSerializer):

    languages=LanguageSerializer(many=True, required=False, read_only=False)

    class Meta:
        model = User
        fields=('id', 'username', 'password', 'email', 'mother_alphabet', 'img', 'languages')

    def create(self, validated_data):
        return User.Objects.create(validated_data)

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields=('id', 'name', 'language', 'icon')

    def create(self, validated_data):
        return Lesson.Objects.create(validated_data)
