from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home),
    path('codes', views.code),
    path('showcode/<int:id>', views.showcode),
    path('search', views.search),
    path('portfolio', views.cv),
    path('register',views.signup),
    path('sendingreq', views.mailapi),
    path('addetails',views.register),
    # path('signin',views.signin),
    # path('logout',views.logout_view),
    path('srpage',views.searchpage),
    path('search1', views.search1),
    path('open_files', views.open_files),
    
]
