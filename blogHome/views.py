from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
#from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from .models import User, UserInfo #Blogs 
from django.contrib import messages
from datetime import timedelta
import datetime
from datetime import datetime as dt
from django.utils import timezone
from django.db.models.functions import TruncMonth
from django.db.models import Count
import random
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
import re

# Create your views here.

def signin(request):
    message = {}
    if request.method == "POST":
        uemail = str(request.POST.get("email"))
        passw = str(request.POST.get("password"))

        User = get_user_model()
            
        try:
            user = User.objects.get(email=uemail)
            user_auth = authenticate(username=uemail, password=passw)
            if user_auth is  None:
                messages.error(request, "Password is not correct try again.")
                message = {"message": "Password is not correct try again."}
                return render(request, "sign-in.html", context=message)
            else:
                url = f"/{user.id}/dashboard/"
                User.objects.filter(id=user.id).update(last_login=timezone.now())
                return redirect(url)
            
            
        except User.DoesNotExist:
            messages.error(request, "User Not Exist")
            message = {"message": "User Not Exist"}
            return render(request, "sign-in.html", context=message)

    return render(request, "sign-in.html")

def signup(request):
    message = {}
    if request.method == "POST":
        uemail = str(request.POST.get("email"))
        passw = str(request.POST.get("password"))
        fname = str(request.POST.get("fname"))
        lname = str(request.POST.get("lname"))
        # Create a new user
 
        try:
            user = User.objects.get(email=uemail)
            messages.error(request, "A user with this email already exists.")
            message = {"message": "A user with this email already exists."}
            return render(request, "sign-up.html", context=message)
        except User.DoesNotExist:
            # Handle the case where the user doesn't exist
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            res = any(chr.isdigit() for chr in passw)
            uppercase = any(ele.isupper() for ele in passw)
            if len(passw) < 8 or  regex.search(passw) == None or res == False or uppercase == False:
                message = {"message": "Password Should contain atleast 1 numeric character, 1 special character, 1 Uppercase character and alphabets with minimum length of 8 "}
                return render(request, "sign-up.html", context=message)                
                
            else:
                username = lname + "." + fname + "." + uemail.split("@")[0]
                user = User(
                    email=uemail,
                    first_name=fname,
                    last_name=lname,
                    date_joined=timezone.now(),
                    is_staff=False,
                    is_superuser=False,
                    is_active=True
                )
                user.set_password(passw)
                user.save()
                userData = User.objects.get(email=uemail)

                userInfo = UserInfo(userName=username.lower(), user_id=userData.id)
                userInfo.save()

                messages.success(
                    request,
                    f"You have successfully signed up. User Name is {username.lower()} ",
                )
                message = {
                    "message": f"You have successfully signed up. User Name is {username.lower()} "
                }
                return render(request, "sign-in.html", context=message)
    return render(request, "sign-up.html")
