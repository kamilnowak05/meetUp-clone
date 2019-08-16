from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from app.permissions import IsOwnerOrAdminOrReadOnly, IsOwnerGroupOrReadOnly

from django.db.models import Q
from events.api.serializers import EventCategorySerializer, EventSerializer, \
    EventMemberSerializer, EventReviewSerializer
from events.models import Event, EventCategory, EventReview


class EventCategoryView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = EventCategorySerializer
    queryset = EventCategory.objects.all()


class ListEventView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        member = self.request.GET.get('member')
        title = self.request.GET.get('title')
        category = self.request.GET.get('category')
        event_id = self.request.GET.get('id')
        if member:
            queryset = queryset.filter(member=member)
        if title:
            queryset = queryset.filter(
                Q(title__icontains=title)
            )
        if category:
            queryset = queryset.filter(
                Q(category=category)
            )
        if event_id:
            queryset = queryset.filter(id=event_id)
        return queryset


class CreateEventView(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class ManageEventView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsOwnerGroupOrReadOnly]

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset


class EventReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrAdminOrReadOnly]
    serializer_class = EventReviewSerializer

    def get_queryset(self):
        queryset = EventReview.objects.all()
        user = self.request.GET.get('user')
        q = self.request.GET.get('q')
        if user:
            queryset = queryset.filter(user=user)
        if q:
            queryset = queryset.filter(review__icontains=q)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventMemberView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = EventMemberSerializer
    queryset = Event.objects.all()

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
