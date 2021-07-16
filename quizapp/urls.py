from django.urls import path, include
from quizapp import views

urlpatterns = [
    path('detailquiz/', views.detailquiz, name='detailquiz'),
    path('detailquiznote/', views.detailquiznote, name='detailquiznote'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiznote/', views.quiznote, name='quiznote'),
]