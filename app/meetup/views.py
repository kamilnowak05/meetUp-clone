from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import generics, views
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from app.permissions import *

from django.db.models import Q
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import *
from .models import Event, EventCategory, EventReview, EventBooking
from django.db.models import Q


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrAdminOrReadOnly]
    serializer_class = EventSerializer
    def get_queryset(self):
        query = Event.objects.all()
        if(self.request.GET.get('approved') == 'true'):
            query = query.filter(approved=True)
        if(self.request.GET.get('approved') == 'false'):
            query = query.filter(approved=False)
        if(self.request.GET.get('no')):
            no = self.request.GET.get('no')
            query = query[:no]
        if(self.request.GET.get('user')):
            query = query.filter(user=self.request.GET.get('user'))
        if(self.request.GET.get('q')):
            query = query.filter(
                Q(title__icontains=self.request.GET.get('q'))
            )
        if(self.request.GET.get('category')):
            query = query.filter(
                Q(category=self.request.GET.get('category'))
            )
        return query


class EventCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer


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

class EventBookingViewSet(viewsets.ModelViewSet):
    permission_classes = [ IsOwnerOrAdminOrReadOnly]
    serializer_class = EventBookingSerializer
    def get_queryset(self):
        queryset = EventBooking.objects.all()
        user = self.request.GET.get('user')
        q = self.request.GET.get('q')
        if(user):
            print(user)
            queryset = queryset.filter(user=user)
        if(q):
            queryset = queryset.filter(event__title__icontains=q)
        return queryset

class EventBookingCreate(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]
    queryset = EventBooking.objects.all()
    serializer_class = EventBookingCreateSerializer

class ApproveEvent(views.APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        event_id = request.GET.get('event')
        event = Event.objects.get(id=event_id)
        if event:
            event.approved = True
            event.save()
            return Response({"message":"Event Approved"}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid url"}, status=status.HTTP_400_BAD_REQUEST)

class ActivateCategory(views.APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        category = request.GET.get('category')
        activate = request.GET.get('activate')
        category = EventCategory.objects.get(id=category)
        if category:
            if activate == str(1):
                category.active = True
                category.save()
                return Response({"message":"Category Activated"}, status=status.HTTP_200_OK)
            elif activate == str(0):
                category.activate = False
                category.save()
                return Response({"message":"Category Deactivated"}, status=status.HTTP_200_OK)
        return Response({"message": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)