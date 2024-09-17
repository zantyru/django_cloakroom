from rest_framework import serializers
from cloakroom.models import Badge


class BadgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Badge
        fields = ["id", "label", "state"]
