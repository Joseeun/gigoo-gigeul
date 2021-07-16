from django.urls import path, include
from challengeapp import views

urlpatterns = [
    path('addchallengeandsearch/', views.addchallengeandsearch, name='addchallengeandsearch'),
    path('addchallenge/', views.addchallenge, name='addchallenge'),
    path('detailchallenge/', views.detailchallenge, name='detailchallenge'),
    path('activity/', views.activity, name='activity'),
    path('mypage/', views.mypage, name='mypage'),
    path('newpost/', views.newpost, name='newpost'),
    path('badge/', views.badge, name='badge'),
]