from django.contrib import messages
from django.db.models.fields import NullBooleanField
from django.shortcuts import render
from .models import exp, newcodes
from django.core.mail import send_mail
from django.conf import settings

# Google sheets api imports
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account


#data sheet for user
# https://docs.google.com/spreadsheets/d/e/2PACX-1vT11YCk4k1K_anGnGmDQCUncujTmeIYAdC5aezURJM9CVlARhenVrtf5R2AD80eTdlqqmGRHDysR1qe/pubhtml?gid=0&single=true
# Create your views here.

def Home(request):   
    return render(request,"index.html")

def code(request):
    programs=newcodes.objects.all();
    param={'programs':programs,'range':range(0,len(programs))}
    return render(request,"allcodes.html",param)

def search(request):
    querrycode=request.GET.get('search')
    programs=newcodes.objects.filter(fullname__contains=querrycode);
    if len(programs)==0:
        k="Nothing found "
    params={'searched':querrycode,'programs':programs,'range':range(0,len(programs))}
    return render(request,"search.html",params)

def cv(request):
    experience=exp.objects.all();
    param={'programs':experience,'range':range(0,len(experience))}
    return render(request,"CV.html",param)

def showcode(request,id):
    programs=newcodes.objects.get(id=id)
    fileurl=str(programs.codefile.url)
    fileurlnew=fileurl.replace('/', '', 1)
    print(fileurl)
    f = open(fileurlnew, 'r')
    file_content = f.read()
    f.close()
    context = {'file_content': file_content,'programs':programs}
    return render(request,"Codes.html",context)


def signup(request):
    return render(request,"register.html")


def books(request):
    params={}
    return render(request,"books.html",params)

def mailapi(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        desc = request.POST.get('desc')
        to="nandanv99@gmail.com"
        print(user,desc)
        param={"message":messages.success(request, "Request sent." ),"name":user}
        print("sended mail successfully.")
        submail="Request from user " +user
        send_mail(submail,desc,settings.EMAIL_HOST_USER,[to])
        return(render(request,"reqsend.html",param))
    else:
        return(print("mail not sent"))