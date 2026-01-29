from django.db import models
from django.conf import settings
from tickets.models import Ticket



class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="bookings")
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "ticket"], name="unique_user_ticket_booking")
        ]
