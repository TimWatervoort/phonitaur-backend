from rest_framework import serializers
from .models import PhonitaurUser, Language, Lesson, Question
import json

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields=('id', 'name', 'img', 'text_color')

    def create(self, validated_data):
        instance = Language.objects.create(
            name=validated_data['name'],
            img=validated_data['img'],
            text_color=validated_data['text_color'],
        )
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.img = validated_data.get('img', instance.img)
        instance.text_color = validated_data.get('text_color', instance.text_color)
        instance.save()
        return instance



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields=('id', 'name', 'question_text', 'answer')

    def create(self, validated_data):
        instance = Question.objects.create(
            name=validated_data['name'],
            question_text=validated_data['question_text'],
            answer=validated_data['answer'],
        )
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.answer = validated_data.get('answer', instance.answer)
        instance.save()
        return instance

class LessonSerializer(serializers.ModelSerializer):

    questions=QuestionSerializer(many=True, required=False, read_only=False)

    class Meta:
        model = Lesson
        fields=('id', 'name', 'language', 'lesson_text', 'icon', 'level', 'questions')

    def create(self, validated_data):
        instance = Lesson.objects.create(
            name=validated_data['name'],
            language=validated_data['language'],
            lesson_text=validated_data['lesson_text'],
            level=validated_data['level']
        )
        instance.save()
        return instance

    def update(self, instance, validated_data):

        if 'questions' in validated_data:
            questions = []
            for i in validated_data['questions']:
                newi = json.loads(json.dumps(i))
                q = Question.objects.get(name = newi['name'])
                questions = questions + [q]

        if 'icon' in validated_data:
            instance.icon = validated_data['icon']

        instance.questions.set(questions)
        instance.name = validated_data.get('name', instance.name)
        instance.language = validated_data.get('language', instance.language)
        instance.lesson_text = validated_data.get('lesson_text', instance.lesson_text)
        instance.level = validated_data.get('level', instance.level)
        instance.save()
        return instance

class PhonitaurUserSerializer(serializers.ModelSerializer):

    languages=LanguageSerializer(many=True, required=False, read_only=False)
    lessons=LessonSerializer(many=True, required=False, read_only=False)

    class Meta:
        model = PhonitaurUser
        fields=('id', 'username', 'password', 'email', 'mother_alphabet', 'img', 'languages', 'lessons')
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

        languages=instance.languages
        lessons=instance.lessons

        if 'languages' in validated_data:
            languages = []
            for i in validated_data['languages']:
                newi = json.loads(json.dumps(i))
                lang = Language.objects.get(name = newi['name'])
                languages = languages + [lang]

        if 'lessons' in validated_data:
            lessons = []
            for i in validated_data['lessons']:
                newi = json.loads(json.dumps(i))
                less = Lesson.objects.get(pk = newi['id'])
                lessons = lessons + [less]

        if 'img' in validated_data:
            instance.img = validated_data['img']

        instance.languages.set(languages)
        instance.lessons.set(lessons)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.mother_alphabet = validated_data.get('mother_alphabet', instance.mother_alphabet)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
