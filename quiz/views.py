from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from quiz.models import Question
from quiz.models import Quizzes
from quiz.serializers import QuestionSerializer
from quiz.serializers import QuizSerializer
from quiz.serializers import RandomQuestionSerializer


class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class RandomQuestion(APIView):

    def get(self, request, format:None, **kwargs):
        question = Question.objects.filter(
            quiz__title=kwargs['topic']
        )
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):

    def get(self, request, format:None, **kwargs):
        quiz = Quiz.objects.filter(
            quiz__title=kwargs['topic']
        )
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)