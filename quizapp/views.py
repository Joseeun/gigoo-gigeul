from django.shortcuts import render
from main.models import Quiz, Quiz_mypage

# Create your views here.
def detailquiz(request):
    return render(request, 'quizapp/detailquiz.html')

def detailquiznote(request):
    return render(request, 'quizapp/detailquiznote.html')

def quiz(request):
    return render(request, 'quizapp/quiz.html')

def quiznote(request):
    return render(request, 'quizapp/quiznote.html')

