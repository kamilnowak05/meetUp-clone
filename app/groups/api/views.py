from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from groups.api.serializers import AppGroupSerializer


class AppGroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AppGroupSerializer
    queryset = AppGroup.objects.all()
