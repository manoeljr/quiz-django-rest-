from django.urls import path

from quiz.views import Quiz
from quiz.views import RandomQuestion

app_name = 'quiz'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('/<str:topic>/', RandomQuestion.as_view(), name='random'),
]