from rest_framework import serializers
from django.db import transaction
from rest_framework.exceptions import ValidationError
from .models import Booking
from tickets.models import Ticket

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "ticket", "quantity", "created_at"]
        read_only_fields = ["created_at"]

    def validate(self, data):
        user = self.context["request"].user
        ticket = data["ticket"]
        qty = data.get("quantity", 1)

        if Booking.objects.filter(user=user, ticket=ticket).exists():
            raise ValidationError("Siz bu ticketni allaqachon bron qilgansiz.")

        if ticket.quantity < qty:
            raise ValidationError("Ticketlar yetarli emas.")

        return data

    def create(self, validated_data):
        user = self.context["request"].user
        ticket = validated_data["ticket"]
        qty = validated_data["quantity"]

        with transaction.atomic():
            ticket = Ticket.objects.select_for_update().get(id=ticket.id)

            if ticket.quantity < qty:
                raise ValidationError("Ticketlar tugagan.")

            ticket.quantity -= qty
            ticket.save()

            booking = Booking.objects.create(
                user=user,
                ticket=ticket,
                quantity=qty
            )

        return booking
