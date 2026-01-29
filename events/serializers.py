from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.phone")

    class Meta:
        model = Event
        fields = ["id", "owner", "title", "description", "date", "category", "created_at"]
