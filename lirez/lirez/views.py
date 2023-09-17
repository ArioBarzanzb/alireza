from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, authenticate, logout
import json
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from .models import User

def home(request):
    return render(request, "lirez/home.html")

def courses(request):
    return render(request, "lirez/courses.html")

def staff(request):
    return render(request, "lirez/staff.html")

def dashboard(request):
    return render(request, "lirez/dashboard.html")

def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "lirez/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "lirez/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "lirez/register.html")
    
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "lirez/login.html", {"message": "Invalid Credentials"})
    return render(request, "lirez/login.html")
