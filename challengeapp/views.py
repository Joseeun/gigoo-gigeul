from django.shortcuts import render
from main.models import Challenge, Activity, Challenge_mypage, Stamp, N_badge, Challenge_Badge

# Create your views here.
def addchallengeandsearch(request):
    return render(request, 'challengeapp/addchallengeandsearch.html')

def addchallenge(request):
    return render(request, 'challengeapp/addchallenge.html')

def detailchallenge(request):
    return render(request, 'challengeapp/detailchallenge.html')

def activity(request):
    return render(request, 'challengepp/activity.html')

def mypage(request):
    return render(request, 'challengepp/mypage.html')

def newpost(request):
    return render(request, 'challengepp/newpost.html')

def badge(request):
    return render(request, 'challengepp/badge.html')
