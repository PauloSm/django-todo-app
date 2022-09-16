from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class MoveSerializer(serializers.Serializer):
    to = serializers.IntegerField()
    node = serializers.IntegerField()
    pos = serializers.CharField(default="first-child")


class UpdateParentSerializer(serializers.Serializer):
    node = serializers.IntegerField()


class MarkSerializer(serializers.Serializer):
    complete = serializers.BooleanField(default=False)
