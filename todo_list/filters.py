from django_filters import rest_framework as dj_filters
from .models import Task


class TaskFilterSet(dj_filters.FilterSet):

    name = dj_filters.CharFilter(field_name="name", lookup_expr="icontains")
    is_active = dj_filters.CharFilter(field_name="is_active", lookup_expr="icontains")
    order_by_field = "timestamp_created"

    class Meta:
        model = Task
        fields = ["name", "is_active"]
