"""signal_soriwa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from soriwa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('emotion/', views.emotion, name='emotion'),
    path('motion/', views.motion, name='motion'),
    path('menu/', views.menu, name="menu"),
    path('game/', views.game, name="game"),
    path('emotion_analysis/', views.emotion_analysis, name='emotion_analysis'),
    path('analysis_result/', views.analysis_result, name='analysis_result'),
    path('result/', views.result, name='result'),
]
