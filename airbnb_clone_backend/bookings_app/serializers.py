from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        if data['end_date'] <= data['start_date']:
            raise serializers.ValidationError("End date must be after start date.")
        return data