from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ContentViewSet, TopicViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'contents', ContentViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),

]