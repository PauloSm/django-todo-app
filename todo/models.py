from django.db import models

from treebeard.mp_tree import MP_Node


class Todo(MP_Node):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    is_complete = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return "{} - (Is Complete: {}) [{}]".format(self.name, self.is_complete, self.id)
