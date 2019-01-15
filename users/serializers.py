from rest_framework import serializers
from .models import User, Language

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields=('id', 'name', 'img')

    def create(self, validated_data):
        return Language.objects.create(validated_data)

class UserSerializer(serializers.ModelSerializer):

    languages=LanguageSerializer(many=True, required=False, read_only=False)

    class Meta:
        model = User
        fields=('id', 'username', 'password', 'email', 'mother_alphabet', 'img', 'languages')

    def create(self, validated_data):
        return User.Objects.create(validated_data)
