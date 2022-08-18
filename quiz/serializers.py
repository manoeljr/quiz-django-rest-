from rest_framework import serializers

from quiz.models import Answer
from quiz.models import Question
from quiz.models import Quizzes


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['title', 'answer']


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = ['title',]


class RandomQuestionSerializer(serializers.ModelSerializer):
    answer = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['title', 'answer',]


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['title', 'answer', 'quiz',]