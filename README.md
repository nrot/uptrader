# uptrader
Testing task

Очень жаль что я не успел доделать. Идея заключается в том что у нас меню и слои, последнии два слоя могут иметь дочернии списки. Для json формата наилучший способ, сделать объекты меню, со списком слоев для каждого и возможными подслоями для некоторых. Я успел написать только для случаев когда слоев 0 или 1. Так как я сделал возможность отрисовывать на одной странице несколько меню с разной глубиной вложености. Количество и глубина слоев ограниченно только максимальной длиной URL.
# Формат URL:
site.domain/menu_MENUNAMEONE/LAYERONE/LAYERTWO/ACTIVELAYER/menu_MENUNAMETWO/LAYERONE/LAYERTWO/ACTIVELAYER
site.domain/(menu_\d+/(\d+/)+)+
Увы регулярные для меня до сих пор не дались, так что могут быть ошибки :(

По идеи такой JSON формат достаточно просто будет разобрать в шаблоне django.

Еще раз очень жаль, что не успел доделать. Хотелось бы попасть на собеседование и хотя бы посмотреть свой уровень навыков и знаний.
