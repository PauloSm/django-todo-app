from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from todo.models import Todo


class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Todo)


admin.site.register(Todo, MyAdmin)
