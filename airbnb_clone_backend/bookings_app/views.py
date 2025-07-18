from rest_framework import viewsets, permissions
from .models import Booking
from .serializers import BookingSerializer
from django_filters.rest_framework import DjangoFilterBackend


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['guest', 'property', 'status']
