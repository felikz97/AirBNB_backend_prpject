from rest_framework import viewsets, permissions
from .models import Review
from .serializers import ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['reviewer', 'property']