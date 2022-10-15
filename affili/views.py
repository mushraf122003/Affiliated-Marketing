from email import message
import imp
from pickle import NONE
import re
from telnetlib import LOGOUT
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import authenticate,login,logout
from register import settings
from django.core.mail import send_mail
from affili.models import profile


# Create your views here.

def home(request):
    return render(request,"index.html")


def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username = username):
            messages.error(request,"Username Already Exist")
            return redirect('signup')
           

        
        if User.objects.filter(email=email):
            messages.error(request,"Email Already Exist")
            return redirect('signup')
        


        if len(username)>15:
            messages.error(request,"Username Must Be Less Than 15 Characters")
            return redirect('signup')

        if pass1!=pass2:
            messages.error(request,"Passwords Not Matches")
            return redirect('signup')
            

        if not username.isalnum():
            messages.error(request,"Username Must Be Alphanumeric")
            return redirect('signup')




        user = User.objects.create_user(username=username,email=email,password=pass1)
        user.first_name = name
        user.last_name = lname

        user.save()

        #DATABASE
        '''user_model = User.objects.get(username=username)
        new_profile = profile.objects.create(user=user_model,id_myuser=user_model)
        new_profile.save()
'''
        messages.success(request, "Your Account HAs Been Sucefully Created")

        # SENDING EMAIL

        subject = "wellcome to our page = django login!!"
        message = "hello " + user.first_name + " !! \n welcome to our website\nconfirm your email address\nthank you."
        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)

        return redirect('signin')




    return render(request, "signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,"index.html",{'fname' : fname})

        else:
            messages.error(request,"Bad Credential")
            return redirect('signin')

    return render(request, "signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Signed Off")
    return redirect('home')