from core.models.publication import Publication

from rest_framework import serializers


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = [
            'id', 'title', 'category'
        ]
