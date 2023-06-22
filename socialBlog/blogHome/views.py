from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
#from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
# from .models import User, Blogs, UserInfo
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
            print(user_auth)
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
