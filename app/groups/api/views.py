from groups.models import AppGroup
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.permissions import IsOwnerOrReadOnly

from groups.api.serializers import AppGroupSerializer, \
    CreateAppGroupSerializer, MembersAppGroupSerializer


class ListAppGroupView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AppGroupSerializer

    def get_queryset(self):
        queryset = AppGroup.objects.all()
        owner = self.request.GET.get('owner')
        group_id = self.request.GET.get('id')
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
    lookup_url_kwarg = 'group_id'

    def get_queryset(self):
        queryset = AppGroup.objects.all()
        return queryset


class MembersAppGroupView(generics.UpdateAPIView):
    serializer_class = MembersAppGroupSerializer
    lookup_url_kwarg = 'group_id'
    queryset = AppGroup.objects.all()

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


# class AppGroupViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = AppGroupSerializer
#     queryset = AppGroup.objects.all()

    # def create(self, request, *args, **kwargs):
    #     # print(request.data)
    #     group = super().create(self, request, *args, **kwargs)
    #     group.owner_id = self.request.user.id
    #     group.save()
    #     return group


# generics.UpdateApiView


# class GroupMemberViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsOwnerOrReadOnly]
#     serializer_class = GroupMemberSerializer

#     def get_queryset(self):
#         queryset = GroupMember.objects.all()
#         member = self.request.GET.get('member')
#         if member:
#             print(member)
#             queryset = queryset.filter(member=member)
#         return queryset

#     def perform_create(self, serializer):
#         serializer.save(member=self.request.user)

#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return JoinGroupSerializer
#         return GroupMemberSerializer


# class JoinGroupViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = AppGroup.objects.all()
#     serializer_class = JoinGroupSerializer

    # permission_classes = [IsAuthenticatedOrReadOnly]
    # serializer_class = JoinGroupSerializer

    # def get(self, request, format=None, username=None):
    #     to_user = get_user_model().objects.get(username=username)
    #     from_user = self.request.user
    #     follow = None
    #     if from_user.is_authenticated:
    #         if from_user != to_user:
    #             if from_user in to_user.followers.all():
    #                 follow = False
    #                 from_user.following.remove(to_user)
    #                 to_user.followers.remove(from_user)
    #             else:
    #                 follow = True
    #                 from_user.following.add(to_user)
    #                 to_user.followers.add(from_user)
    #     data = {
    #         'follow': follow
    #     }
    #     return Response(data)
    # # def get_queryset(self):
    # #     queryset = JoinGroup.objects.all()
    # #     user = self.request.GET.get('user')
    # #     if(user):
    # #         print(user)
    # #         queryset = queryset.filter(user=user)
    # #     return queryset

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
