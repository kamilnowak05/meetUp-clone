from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.permissions import IsOwnerOrReadOnly
from groups.api.serializers import AppGroupSerializer, CreateAppGroupSerializer, MembersAppGroupSerializer
from groups.models import AppGroup


class ListAppGroupView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AppGroupSerializer

    def get_queryset(self):
        queryset = AppGroup.objects.all()
        owner = self.request.GET.get("owner")
        group_id = self.request.GET.get("id")
        if owner:
            queryset = queryset.filter(owner=owner)
        if group_id:
            queryset = queryset.filter(id=group_id)
        return queryset


class CreateAppGroupView(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CreateAppGroupSerializer
    queryset = AppGroup.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.user.id)


class ManageAppGroupView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppGroupSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = AppGroup.objects.all()
        return queryset


class MembersAppGroupView(generics.UpdateAPIView):
    serializer_class = MembersAppGroupSerializer
    lookup_url_kwarg = "group_id"
    queryset = AppGroup.objects.all()
