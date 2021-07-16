from django.shortcuts import render
from main.models import User

# Create your views here.
def editinfo(request):
    return render(request, 'userapp/editinfo.html')

def findpw(request):
    return render(request, 'userapp/findpw.html')

def signin(request):
    return render(request, 'userapp/signin.html')

def signup(request):
    return render(request, 'userapp/signup.html')



