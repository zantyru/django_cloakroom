from rest_framework import permissions, viewsets
from cloakroom.models import Badge
from restapi.serializers import BadgeSerializer


class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    #permission_classes = [permissions.IsAuthenticated]
