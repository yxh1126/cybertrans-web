from django import template
from rango.models import Category

register = template.Library()


@register.inclusion_tag('rango/cats.html')
def get_category_list(act_cat=None):
    return {
        'cats': Category.objects.all(),
        'act_cat': act_cat
    }


@register.inclusion_tag('rango/timlog.html')
def get_super_title(act_cat=None):
    return {
        'tim_log': "This is a register inclusion tag...",
        'act_cat': act_cat
    }
