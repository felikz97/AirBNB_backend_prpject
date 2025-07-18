from rest_framework import serializers
from .models import Property, PropertyImage
from users_app.models import User
class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image', 'uploaded_at']

class PropertySerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = ['id', 'host', 'title', 'description', 'price_per_night', 'location', 'max_guests', 'created_at', 'images']
        read_only_fields = ['id', 'created_at']