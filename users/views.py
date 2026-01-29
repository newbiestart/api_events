from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import CodeLoginSerializer


class VerifyCodeAPIView(APIView):
    def post(self, request):
        phone = request.data.get("phone")
        code = request.data.get("code")

        try:
            user = User.objects.get(phone=phone, verification_code=code)
            return Response({"detail": "Code is valid"}, status=200)
        except User.DoesNotExist:
            return Response({"error": "Invalid code"}, status=400)


class CodeLoginAPIView(APIView):
    def post(self, request):
        serializer = CodeLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
