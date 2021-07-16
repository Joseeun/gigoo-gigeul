from django.urls import path, include
from userapp import views

urlpatterns = [
    path('editinfo/', views.editinfo, name='editinfo'),
    path('findpw/', views.findpw, name='findpw'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
]