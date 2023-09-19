from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('courses/', views.courses, name="courses"),
    path('staff/', views.staff, name="staff"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("create/", views.create_course, name="create_course"),
]
