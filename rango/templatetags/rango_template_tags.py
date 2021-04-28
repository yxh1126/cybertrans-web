from django import template
from rango.models import Category

register = template.Library()


@register.inclusion_tag('tagview/list_category.html')
def get_category_list(act_cat=None):
    return {
        'cats': Category.objects.all(),
        'act_cat': act_cat
    }
