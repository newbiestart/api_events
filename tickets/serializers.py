from rest_framework import serializers
from .models import Ticket
from events.models import Event

class TicketSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all()
    )
    event_title = serializers.CharField(source="event.title", read_only=True)

    class Meta:
        model = Ticket
        fields = ["id", "event", "event_title", "price", "quantity"]
