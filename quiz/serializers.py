from rest_framework import serializers

from quiz.models import Question
from quiz.models import Quizzes


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = ['title',]


class RandomQuestionSerializer(serializers.ModelSerializer):
    answer = serializers.StringRelatedField(many=True)

    class Meta:
        model = Question
        fields = ['title', 'answer',]