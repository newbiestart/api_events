from django.urls import path
from .views import VerifyCodeAPIView, CodeLoginAPIView

urlpatterns = [
    path("verify/", VerifyCodeAPIView.as_view()),
    path("login-by-code/", CodeLoginAPIView.as_view()),
]
