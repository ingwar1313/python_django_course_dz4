from rest_framework.serializers import ModelSerializer
from .models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        read_only_fields = ["id", "name", "timestamp_created", "timestamp_closed"]
        fields = read_only_fields + ["is_active"]
