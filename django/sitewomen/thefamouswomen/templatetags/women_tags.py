from django import template
from django.db.models import Count

import thefamouswomen.views as views
from thefamouswomen.models import Category, TagPost
from thefamouswomen.utils import menu

register = template.Library()

@register.simple_tag()
def get_menu():
    return menu

@register.inclusion_tag('thefamouswomen/list_categories.html')
def show_categories(catselected = 0):
    cats = Category.objects.annotate(total = Count("posts")).filter(total__gt=0)

    return {'cats': cats, 'cat_selected': catselected}

@register.inclusion_tag('thefamouswomen/list_tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.annotate(total = Count("tags")).filter(total__gt=0)
}