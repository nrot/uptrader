from django import template
from main.models import *

register = template.Library()

# TODO: Доделать
def draw_menu(value):
    menu_obj = Menu.objects.filter(name=value).values()[0]
    print("Menu objects: {0}".format(menu_obj))
    items = itemMenu.objects.filter(parentMenu=menu_obj['id']).values()
    return str(items)

register.filter('draw_menu', draw_menu)
