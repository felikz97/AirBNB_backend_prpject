from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'guest', 'property', 'start_date', 'end_date', 'total_price', 'status', 'created_at']
        read_only_fields = ['id', 'created_at']