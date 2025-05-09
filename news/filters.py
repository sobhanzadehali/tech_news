import django_filters
from django.db import models

from .models import Content,Topic
from django_filters import rest_framework as filters


class ContentFilter(django_filters.FilterSet):
    topics = django_filters.ModelMultipleChoiceFilter(
        field_name='topics__name',
        to_field_name='name',
        queryset=Topic.objects.all()
    )

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