from django import template
from Exam_27_10.utils import get_user_obj

register = template.Library()

@register.simple_tag
def get_user():
    return get_user_obj()