from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "lirez/home.html")

def courses(request):
    return render(request, "lirez/courses.html")

def staff(request):
    return render(request, "lirez/staff.html")

def dashboard(request):
    return render(request, "lirez/dashboard.html")

def register(request):
    return render(request, "lirez/register.html")

def login(request):
    return render(request, "lirez/login.html")