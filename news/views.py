# views.py
import django_filters
from rest_framework import viewsets
from .models import Content
from .serializers import ContentSerializer
from .filters import ContentFilter

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filterset_class = ContentFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]