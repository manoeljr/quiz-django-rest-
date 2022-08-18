from django.contrib import admin

from quiz import models
from quiz.models import Answer
from quiz.models import Category
from quiz.models import Question
from quiz.models import Quizzes


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]


@admin.register(Quizzes)
class QuizzesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',]


class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = ['answer_text', 'is_right']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['title', 'quiz']
    list_display = ['title', 'quiz', 'date_updated']
    inlines = [AnswerInlineModel,]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text', 'is_right', 'question']