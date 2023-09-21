from django import template
from learning.models import Teacher

register = template.Library()

@register.filter
def is_teacher(user):
    return Teacher.objects.filter(email=user.email).exists()