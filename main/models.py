from django.db.models import *

# Create your models here.

class Menu(Model):
    name = CharField(max_length=128)
    def __str__(self):
        return self.name

class itemMenu(Model):
    name = CharField(max_length=128)
    parentMenu = ForeignKey(Menu, on_delete=CASCADE)
    parentItem = ForeignKey('itemMenu', on_delete=CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
