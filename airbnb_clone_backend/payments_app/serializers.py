from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'booking', 'amount', 'payment_date', 'method', 'status']
        read_only_fields = ['id', 'payment_date']
        extra_kwargs = {
            'amount': {'min_value': 0},
            'status': {'default': 'pending'}
        }