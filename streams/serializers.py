from rest_framework import serializers
from .blocks import ServiceBlock
from wagtail.core.models import Page

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ["id", "title", "slug"]

class ServiceBlockSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    text = serializers.CharField()
    button_page = PageSerializer(
        source="get_button_page",
        read_only=True
    )

    class Meta:
        model = ServiceBlock
