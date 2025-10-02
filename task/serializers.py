from rest_framework import serializers
from .models import Task


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "status", "created_at",]
        read_only_fields = ["id", "created_at"]

