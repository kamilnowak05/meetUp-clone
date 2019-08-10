from rest_framework import viewsets, status
from rest_framework import views
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, \
    IsAdminUser, AllowAny

from app.permissions import IsOwnerOrAdminOrReadOnly, IsOwnerOrReadOnly, \
    IsAdminOrReadOnly

from django.db.models import Q
from rest_framework.response import Response
from events.api.serializers import EventCategorySerializer, EventReviewSerializer, \
    EventSerializer, EventMemberSerializer, EventMemberCreateSerializer
from events.models import Event, EventCategory, EventReview, EventMember


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    serializer_class = EventSerializer

    def get_queryset(self):
        query = Event.objects.all()
        if(self.request.GET.get('no')):
            no = self.request.GET.get('no')
            query = query[:no]
        if(self.request.GET.get('user')):
            query = query.filter(user=self.request.GET.get('user'))
        if(self.request.GET.get('title')):
            query = query.filter(
                Q(title__icontains=self.request.GET.get('title'))
            )
        if(self.request.GET.get('category')):
            query = query.filter(
                Q(category=self.request.GET.get('category'))
            )
        return query

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventCategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = EventCategorySerializer
    queryset = EventCategory.objects.all()


class EventReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrAdminOrReadOnly]
    serializer_class = EventReviewSerializer

    def get_queryset(self):
        queryset = EventReview.objects.all()
        user = self.request.GET.get('user')
        q = self.request.GET.get('q')
        if(user):
            print(user)
            queryset = queryset.filter(user=user)
        if(q):
            queryset = queryset.filter(review__icontains=q)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventMemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventMemberSerializer

    def get_queryset(self):
        queryset = EventMember.objects.all()
        user = self.request.GET.get('user')
        q = self.request.GET.get('q')
        if(user):
            print(user)
            queryset = queryset.filter(user=user)
        if(q):
            queryset = queryset.filter(event__title__icontains=q)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventMembersCreateViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = EventMember.objects.all()
    serializer_class = EventMemberCreateSerializer
