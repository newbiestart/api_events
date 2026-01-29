from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


class CodeLoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    code = serializers.CharField()

    def validate(self, data):
        try:
            user = User.objects.get(phone=data["phone"], verification_code=data["code"])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid code")

        user.is_verified = True
        user.verification_code = None
        user.save()

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
