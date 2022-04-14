import re
from sqlite3 import paramstyle
from django.contrib import messages
from django.db.models.fields import NullBooleanField
from django.shortcuts import redirect, render
from .models import exp, newcodes,user1,files
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
# Google sheets api imports
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# Create your views here.
# k={"name":z}
z1={'name':"Login/Signup"}
def Home(request):   
    direct="/static/app/z4app.apk"  
    programs=newcodes.objects.all();
    param={'programs':programs,'range':range(0,len(programs),-1),'first':programs[len(programs)-1],'second':programs[len(programs)-2],'third':programs[len(programs)-3],'range1':programs.count(),'app':direct}
    return render(request,"trial.html",param)

def code(request):
    programs=newcodes.objects.all();
    param={'programs':programs,'range':range(0,len(programs))}
    return render(request,"allcodes.html",param)

def search(request):
    querrycode=request.GET.get('search')
    university=request.GET['university']
    branch=request.GET['branch']
    subject=request.GET['subject']
    sem=request.GET['sem']
    programs=newcodes.objects.filter(fullname__contains=querrycode);
    if len(programs)==0:
        k="Nothing found "
        print("noting found from name ",querrycode)
        programs=newcodes.objects.filter(description__contains=querrycode);
        if(len(programs)!=0):
            print("found from description :",querrycode)
    params={'searched':querrycode,'programs':programs,'range':range(0,len(programs)),'university':university,'branch':branch,'subject':subject,'sem':sem}
    return render(request,"search.html",params)

def cv(request):
    experience=exp.objects.all();
    param={'programs':experience,'range':range(0,len(experience))}
    return render(request,"CV.html",param)

def showcode(request,id):
    programs=newcodes.objects.get(id=id)
    fileurl=str(programs.codefile.url)
    print(fileurl)
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


def register(request):
    name=request.GET.get('name')
    # email=request.GET.get('logemail')
    password=request.GET.get('logpass')
    # print(name,password)
    SAMPLE_SPREADSHEET_ID = '1dR1QxQfCFWSL5PIe5a6xoVP5m2fzZgzQpawRkUN-jdE'
    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="details!A1:B500").execute()
        values = result.get('values', [])
        # print(values)
    except HttpError as err:
        print(err)
    dic=[[name,password]]
    dic1=[[name]]

    request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="details!A1:B500", 
                                    valueInputOption="USER_ENTERED",
                                    body={"values":dic1}).execute()
    request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="passwords!A1:B500", 
                                    valueInputOption="USER_ENTERED",
                                    body={"values":dic}).execute()

    print("Succesfull added")
    return render(request,"register.html")



def searchpage(request):   
    # messages.success("cool")
    programs=newcodes.objects.all()
    params={'range':programs.count()}
    return render(request,"search2.html",params)

def search1(request):
    querrycode=request.GET.get('search')
    # university=request.GET['university']
    # branch=request.GET['branch']
    # subject=request.GET['subject']
    # sem=request.GET['sem']
    programs=newcodes.objects.filter(fullname__contains=querrycode);
    # programs1=newcodes.objects.filter(description__contains=querrycode);
    if len(programs)==0:
        k="Nothing found "
        print("noting found from fullname ",querrycode)
        programs=newcodes.objects.filter(description__contains=querrycode);
        if(len(programs)!=0):
            print("found from description :",querrycode)
    params={'searched':querrycode,'programs':programs,'range':range(0,len(programs))}
    return render(request,"search.html",params)

def open_files(request):
    programs=files.objects.get(id=1);
    param={'prog':programs.files.url}
    return render(request,"books.html",param)

def all_snippet(request):
    snippet=files.objects.all()
    param={'snippet':snippet,'range':range(0,len(snippet))}
    return render(request,"books.html",param)
