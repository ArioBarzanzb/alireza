from django.db import models
from django.contrib.auth.models import AbstractUser



class Teacher(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100)
    resume = models.CharField(max_length=2000)
    email = models.EmailField()
    profile_pic = models.ImageField(blank=True)
    def __str__(self):
        return f'{self.firstname} {self.lastname}'





class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    image = models.ImageField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="courses")



class User(AbstractUser):
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="%(app_label)s_%(class)s_related",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )
    dashboard = models.ManyToManyField(Course, blank=True, related_name="users")



