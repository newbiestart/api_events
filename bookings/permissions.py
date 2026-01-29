from rest_framework.permissions import BasePermission


class IsVerifiedUser(BasePermission):
    message = "Iltimos, Telegram bot orqali tasdiqlang."

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.telegram_id)
