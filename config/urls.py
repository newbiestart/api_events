from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from events.views import EventViewSet
from tickets.views import TicketViewSet
from bookings.views import BookingViewSet

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Event Management API",
        default_version="v1",
        description="Simple Event Booking API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register("events", EventViewSet, basename="events")
router.register("tickets", TicketViewSet, basename="tickets")
router.register("bookings", BookingViewSet, basename="bookings")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("rest_framework.urls")),

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("api/", include(router.urls)),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
]
