import django_filters
from django.db import models

from .models import Content,Topic
from django_filters import rest_framework as filters


class ContentFilter(django_filters.FilterSet):

    topics = django_filters.CharFilter(method='filter_topics', label='filter by topics')

    include_words = django_filters.CharFilter(
        method='filter_include_words',
        label='Include words in title or body'
    )

    exclude_words = django_filters.CharFilter(
        method='filter_exclude_words',
        label='Exclude words from title or body'
    )

    class Meta:
        model = Content
        fields = ['topics']

    def filter_topics(self, queryset, name, value):
        words = value.split(',')
        queryset = queryset.filter(topics__name__in=words)
        return queryset

    def filter_include_words(self, queryset, name, value):
        words = value.split(',')
        for word in words:
            queryset = queryset.filter(
                models.Q(title__icontains=word.strip()) |
                models.Q(body__icontains=word.strip())
            )
        return queryset

    def filter_exclude_words(self, queryset, name, value):
        words = value.split(',')
        for word in words:
            queryset = queryset.exclude(
                models.Q(title__icontains=word.strip()) |
                models.Q(body__icontains=word.strip())
            )
        return queryset