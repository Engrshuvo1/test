from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.views import View
import re
from urllib import request

from django.contrib.auth.hashers import make_password, check_password

from websiteapp.models import *

# Create your views here.

def indexpage(request):
    menues = menus.objects.all()
    context = {
        'menues': menues
    }
    return render(request, "index.html", context)


def aboutpage(request):
    return render(request, "about.html")


def servicepage(request):
    return render(request, "service.html")


def contactpage(request):
    return render(request, "contact.html")


def signin(request):
    return render(request, "signin.html")



class signup(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        fname = request.POST['fname']

        lname = request.POST['lname']
        fullname = fname +" "+ lname
        
        joinname = ''.join(fullname)
        replacedot = joinname.replace('.', '')
        spaceremove = re.sub(r"\s+", '', replacedot)
        username = spaceremove.upper()
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        values = { 
            'first_name':fname, 
            'last_name':lname, 
            'mobile':mobile, 
            'email':email, 
        }

        Error_Message = None

        if not fname:
            Error_Message = "First name is required!!"
        elif len(fname) < 2:
            Error_Message = "First name must be 2 charter or more!!"
        elif not lname:
            Error_Message = "Last name is required!!"
        elif len(lname) < 4:
            Error_Message = "Last name must be 2 charter or more!!"
        elif not mobile:
            Error_Message = "Mobile number is required!!"
        elif len(mobile) < 11:
            Error_Message = "Mobile number must be 11 digit!!"
        elif not email:
            Error_Message = "Email is required!!"
        # elif str(email).endswith("@gmail.com"):
        #     Error_Message = "Please check the email @ option!!"
        elif not password:
            Error_Message = "Password must be required!!"
        elif len(password) < 6:
            Error_Message = "password must be 6 charter or more!!"
        elif not repassword:
            Error_Message = "Repassword must be required!!"
        elif len(password) < 6:
            Error_Message = "Repassword must be 6 charter or more!!"

        if password == repassword:
            if User.objects.filter(email=email).exists():
                Error_Message = "Email is allready registered!!"
                context = {
                    'Message' : Error_Message,
                    'value' : values,
                }
                return render(request, 'signup.html', context)
            else:
                if User.objects.filter(username=mobile).exists():
                    Error_Message = "Mobile is allready registered!!"
                    context = {
                        'Message' : Error_Message,
                        'value' : values,
                    }
                    return render(request, 'signup.html', context)
                else:
                    if not Error_Message:
                        newuser =User(first_name=fname, last_name=lname, username=username, password=make_password(password), email=email, is_staff = True)
                        newuser.save()
                        return redirect('signinpage')
                    else:
                        Error_Message = Error_Message
                        context = {
                        'Message' : Error_Message,
                        'value' : values,
                    }
                    return render(request, 'signup.html', context)
        else:
            Error_Message = "Password did not Match!!"
            context = {
                'Message' : Error_Message,
                'value' : values,
                }
            return render(request, 'signup.html', context)
    















class stuadmin(View):
    def get(self, request):
        return render(request, "stuadmin.html")

    def post(self, request):
        pass

class stunotess(View):
    def get(self, request):
        subjects = subjectsix.objects.all()
        notes = stunotes.objects.all()
        totlanote = stunotes.objects.all().count()
        print(totlanote)
        context = {
            "subjects":subjects,
            'notes':notes,
            'totlanote':totlanote
        }
        return render(request, "stunotes.html", context)

    def post(self, request):
        subject = request.POST['subject']
        title = request.POST['title']
        descriptions = request.POST['descriptions']

        Error_Message = None
        if not title:
            Error_Message = "Title must be requried!!"
        elif not descriptions:
            Error_Message = "Descriptions nust be requried!!"
        if not Error_Message:
            newdata =stunotes(classname="06", subject=subject, title=title, descriptions=descriptions)
            newdata.save()
            return redirect('stunotess')

class stunoteupdate(View):
    def get(self, request, id):
        subjects = subjectsix.objects.all()
        notes = stunotes.objects.get(pk=id)
        context = {
            "subjects":subjects,
            'notes':notes
        }
        return render(request, "stunoteupdate.html", context)

    def post(self, request,id):
        notes = stunotes.objects.get(pk=id)
        subject = request.POST['subject']
        title = request.POST['title']
        descriptions = request.POST['descriptions']

        notes.subject = subject
        notes.title = title
        notes.descriptions = descriptions
        notes.save()

        return redirect('stunotess')


class stuhomeworks(View):
    def get(self, request):
        title = " Student Home Works ". center(60, "-")
        context = {
            "ptitle":title,
        }
        return render(request, "stuhomeworks.html", context)

    def post(self, request):
        pass

class stulistview(View):
    def get(self, request):
        title = " Student Home Works ". center(60, "-")
        context = {
            "ptitle":title,
        }
        return render(request, "stulistview.html", context)

    def post(self, request):
        pass


class teaadmin(View):
    def get(self, request):
        return render(request, "teaadmin.html")

    def post(self, request):
        pass

class teaclass06(View):
    def get(self, request):
        return render(request, "teaclass06.html")

    def post(self, request):
        pass 

class teacherslist(View):
    def get(self, request):
        return render(request, "teacherslist.html")

    def post(self, request):
        pass


