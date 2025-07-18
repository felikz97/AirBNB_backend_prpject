from rest_framework import viewsets, permissions
from .models import Payment
from .serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Validate payment logic, prevent double payment
        booking = serializer.validated_data['booking']
        if hasattr(booking, 'payment'):
            raise serializer.ValidationError('Payment already exists for this booking.')
        serializer.save(status='pending')