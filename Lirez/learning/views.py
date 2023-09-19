from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, authenticate, logout
import json
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from .models import User
from .models import Teacher

def home(request):
    return render(request, "learning/home.html")

def courses(request):
    return render(request, "learning/courses.html")

def staff(request):
    return render(request, "learning/staff.html", {"teachers": Teacher.objects.all()})

@login_required
def dashboard(request):
    return render(request, "learning/dashboard.html")

def register(request):
    if request.method == "POST":
        usertype = request.POST["user_type"] 
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "learning/register.html", {
                "message": "Passwords must match."
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
            if usertype == "teacher":
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                resume = request.POST['resume']
                teacher = Teacher(firstname=firstname, lastname=lastname, resume=resume, email=email)
                teacher.save()
        except IntegrityError as e:
            print(e)
            return render(request, "learning/register.html", {
                "message": "Email address already taken."
            })
        
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "learning/register.html")
    
    
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
            return render(request, "learning/login.html", {"message": "Invalid Credentials"})
    return render(request, "learning/login.html")

@login_required
def create_course(request):
    if request.method == "POST":
        return HttpResponse("POST")
    return render(request, "learning/create.html")