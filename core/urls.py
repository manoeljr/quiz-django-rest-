from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('quiz/', include('quiz.urls', namespace='quiz')),
    path('admin/', admin.site.urls),
]
