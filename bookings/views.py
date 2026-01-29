from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import BookingSerializer
from .models import Booking

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
