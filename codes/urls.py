from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('codes', views.code),
    path('showcode/<int:id>', views.showcode),
    path('search', views.search),
    path('portfolio', views.cv),
    path('signup',views.signup),
    path('sendingreq', views.mailapi),
]