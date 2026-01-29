from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied

from .models import Ticket
from .serializers import TicketSerializer



class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Ticket.objects.select_related("event").all()

    def perform_create(self, serializer):
        event = serializer.validated_data["event"]
        if event.owner != self.request.user:
            raise PermissionDenied("Bu event sizniki emas")
        serializer.save()
