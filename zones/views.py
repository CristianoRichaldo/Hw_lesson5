from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Zone, Visitors
from .serializer import ZoneSerializer, VisitorsSerializer


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields = ['location']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'location', 'created_at']


class VisitorsViewSet(viewsets.ModelViewSet):
    queryset = Visitors.objects.all()
    serializer_class = VisitorsSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields = ['is_allowed', 'zone']
    search_fields = ['full_name', 'info']
    ordering_fields = ['full_name', 'created_at']
