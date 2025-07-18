from rest_framework import viewsets, permissions
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for booking operations.
    - Admins can view all bookings
    - Authenticated users can view/create/update their own
    """
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'  # Optional: lets you use /bookings/{id}/ explicitly

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(guest=user)

    def perform_create(self, serializer):
        serializer.save(guest=self.request.user)
