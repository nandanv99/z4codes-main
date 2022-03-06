from django.contrib import messages
from django.db.models.fields import NullBooleanField
from django.shortcuts import render
from .models import exp, newcodes,user1
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



def signin(request):
    name=request.GET.get('logname')
    passw=request.GET.get('logpass')
    print(name,passw)
    SAMPLE_SPREADSHEET_ID = '1dR1QxQfCFWSL5PIe5a6xoVP5m2fzZgzQpawRkUN-jdE'
    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="passwords!A1:B500").execute()
        values = result.get('values', [])
    except HttpError as err:
        print(err)

    for i in values:
        if(i[0].upper()==name.upper() and i[1]==passw):
            print("Founded")
            # user1 = User.objects.create_user(name, 'example@gmail.com', passw)
            # user1.name=name
            # user1.passwor=passw
            # user1.save()
            # print("hello")
            # user = authenticate(username=name, password=passw)
            # print("loged in")
            # if user is not None:
            #     login(request, user)
            #     print("login1")
            return HttpResponse("login successfully")
        else:
            print("User not found")
    return HttpResponse("error")

def logout_view(request):
    logout(request)
    return HttpResponse("Logout successfully")