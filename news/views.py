# views.py
import django_filters
from rest_framework import viewsets
from .models import Content, Topic, Comment
from .serializers import ContentSerializer, TopicSerializer, CommentSerializer
from .filters import ContentFilter

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all().order_by('-created_at')
    serializer_class = ContentSerializer
    filterset_class = ContentFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer