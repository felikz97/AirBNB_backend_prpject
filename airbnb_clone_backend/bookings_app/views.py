from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(guest=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.guest != request.user:
            return Response({'detail': 'Only the guest who booked can update this.'}, status=403)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.guest != request.user:
            return Response({'detail': 'Only the guest who booked can cancel this.'}, status=403)
        return super().destroy(request, *args, **kwargs)
