from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

default_filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]