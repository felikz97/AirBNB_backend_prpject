from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Property
from .serializers import PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Automatically associate host with logged-in user
        serializer.save(host=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.host != request.user:
            return Response({'detail': 'You can only update your own property.'}, status=403)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.host != request.user:
            return Response({'detail': 'You can only delete your own property.'}, status=403)
        return super().destroy(request, *args, **kwargs)
