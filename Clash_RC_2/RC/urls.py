"""clashrc1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('adminpanel/', admin.site.urls),
    path('', views.home, name='home'),
    path('question/', views.questions, name='questions'),
    path('Submission/', views.Submission, name='submissions'),
    path('question/<int:id>', views.question, name='question'),
    path('question_sub/<int:id>', views.question_sub, name='question_sub'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('register/', views.userRegister, name='register'),
    path('settingwale/', views.settingwale, name='settingwale'),
    path('test/', views.test, name='test'),

]
