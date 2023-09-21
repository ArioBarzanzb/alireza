from django.contrib.auth import login, authenticate, logout
import json
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render, redirect,  get_object_or_404
from django.urls import reverse
from .models import User, Teacher, Course
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Count
from urllib.parse import urlparse, parse_qs
# from pytube import YouTube
def home(request):
    popular_courses = Course.objects.annotate(user_count=Count('users')).order_by('-user_count')[:4]
    return render(request, 'learning/home.html', {'popular_courses': popular_courses})

def courses(request):
    return render(request, "learning/courses.html", {"courses": Course.objects.all()})

def staff(request):
    return render(request, "learning/staff.html", {"teachers": Teacher.objects.all()})

@login_required
def dashboard(request):
    dashboard_courses = request.user.dashboard.all()
    return render(request, "learning/dashboard.html", {'dashboard_courses': dashboard_courses})




@login_required
def toggle_dashboard(request, course_id):
    course = get_object_or_404(Course, id=course_id)
   
    if course in request.user.dashboard.all():
        request.user.dashboard.remove(course)
    else:
        request.user.dashboard.add(course)
    
    return redirect('dashboard')  # Replace 'dashboard' with the name of your dashboard URL pattern


def course_view(request):
    return render(request, "learning/course.html")



# For Course Page

# def youtube_to_iframe(request):
#     context = {}
#     if request.method == 'POST':
#         youtube_link = request.POST.get('youtube_link')
#         try:
#             yt = YouTube(youtube_link)
#             video_url = yt.streams.filter(progressive=True, file_extension='mp4').first().url
#             context['video_url'] = video_url
#         except Exception as e:
#             context['error_message'] = str(e)
#     return render(request, 'learning/course.html', context)


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
            # Check if all required fields are filled
            if not all([request.POST.get(field) for field in ['firstname', 'lastname', 'resume', 'email', 'password']]):
                return render(request, "learning/register.html", {
                    "message": "All fields must be filled."
                })

            if usertype == "teacher":
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                resume = request.POST['resume']
                profile_pic = request.FILES.get("profile_pic", None)

                # Check if teacher's input is correct (add your own conditions)
            if not firstname.isalpha() or not lastname.isalpha():
                return render(request, "learning/register.html", {
                    "message": "Invalid input for teacher's name."
                })

            teacher = Teacher(firstname=firstname, lastname=lastname, resume=resume, email=email, profile_pic=profile_pic)
            teacher.save()

            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create_user(email, email, password)
            user.save()

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

def create_course(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        image = request.FILES["image"] 
        teacher = Teacher.objects.get(email=request.user.email)
        course = Course(title=title, description=description, image=image, teacher=teacher)
        course.save()
        return HttpResponseRedirect(reverse("home"))
    return render(request, "learning/create.html")