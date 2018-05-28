from django.shortcuts import render
from django.http import *
from main.models import *
import json
# Create your views here.

# def recursiv(obj, menu, items, step):
#     if step == len(items):
#         pass
#     elif step + 1 == len(items):
#         pass
#     elif step == 0:
#         obj[menu.name] = []
#


def index(request, items):
    print('Items: {0}'.format(items))
    menus_list = items.split('menu_')
    print('Menus: {0}'.format(menus_list))
    draw_object = {}
    for m in menus_list:
        if m == '':
            continue
        if m[-1] == '/':
            ims = m[:-1].split('/')
        else:
            ims = m.split('/')
        menu = ims[0]
        ims = ims[1:]
        print('Menu: {0}'.format(menu))
        print('ItemsMenu: {0}'.format(ims))
        menu_obj = Menu.objects.filter(name=menu).values().first()
        print("Menu objects: {0}".format(menu_obj))
        # recursiv(draw_object, menu_obj, ims, 0)
        if menu_obj is None:
            continue
        draw_object[menu] = []
        smth = itemMenu.objects.filter(parentMenu=menu_obj['id'], parentItem__isnull=True).values()
        if len(ims) == 0:
            draw_object[menu].append([])
            print('Draw object: {0}'.format(draw_object))
            for x, i in enumerate(list(smth)):
                draw_object[menu][0].append({i['name']: []})
            return HttpResponse(json.dumps(draw_object))
        for x, i in enumerate(ims):
            print("X: {0}; I: {1}".format(x,i))
            draw_object[menu].append([])
        chosen = itemMenu.objects.filter(name=ims[-1]).first()
        childs_chosen = list(itemMenu.objects.filter(parentItem=chosen.id).values())
        print("Count: {0}".format(childs_chosen))
        if len(ims) == 1:
            for x, i in enumerate(list(smth)):
                draw_object[menu][0].append({i['name']: []})
            for i in childs_chosen:
                draw_object[menu][0][-1][ims[-1]].append(i['name'])
            return HttpResponse(json.dumps(draw_object))
        print('Draw object: {0}'.format(draw_object))

        for i, l in enumerate(ims):
            draw_object[menu][i].append({l: []})
        for i in childs_chosen:
            draw_object[menu][-1][-1][ims[-1]].append(i['name'])
        print('Draw object: {0}'.format(draw_object))

        # for i in ims:
           # print("draw_object: {0}".format(draw_object))
           # draw_object[menu].append({i: []})
        # ims_1_object = itemMenu.objects.filter(name=ims[-1])[0]
        # draw_object[menu][-1][ims[-1]] = list(itemMenu.objects.filter(parentItem=ims_1_object.id).values())
        # print("Draw object: {0}".format(draw_object))

    return HttpResponse(json.dumps(draw_object))
