from rest_framework import serializers
from .models import Zone, Visitors

class VisitorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitors
        fields = '__all__'

class ZoneSerializer(serializers.ModelSerializer):
    visitors = VisitorsSerializer(many=True, read_only=True)
    visitors_count = serializers.IntegerField(
        source = 'visitors.count',
        read_only = True
    )
    class Meta:
        model = Zone
        fields = '__all__'