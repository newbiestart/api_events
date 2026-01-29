from rest_framework.permissions import BasePermission

class IsEventOwner(BasePermission):
    def has_permission(self, request, view):
        if view.action == "create":
            event_id = request.data.get("event")
            if not event_id:
                return False
            return request.user.events.filter(id=event_id).exists()
        return True
