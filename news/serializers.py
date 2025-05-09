from rest_framework import serializers
from .models import Topic, Content, Comment


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    class Meta:
        model = Content
        fields = ['title', 'slug', 'body', 'created_at', 'cover_image', 'author', 'comments']

    def get_comments(self, obj):
        comments = obj.comments.filter(parent__isnull=True).order_by('-created_at')
        return CommentSerializer(comments, many=True).data


class RecursiveField(serializers.Field):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    replies = RecursiveField(read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    user = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user','likes_count', 'replies', 'created_at')