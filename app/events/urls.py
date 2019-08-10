from django.urls import path, include

from events.api.views import EventViewSet, EventCategoryViewSet, \
    EventReviewViewSet, EventMemberViewSet

from rest_framework.routers import DefaultRouter


app_name = 'events'

router = DefaultRouter()
router.register(r'events', EventViewSet, base_name='events')
router.register(r'event-category', EventCategoryViewSet,
                base_name='event-category')
router.register(r'event-review', EventReviewViewSet, base_name='event-review')
router.register(r'event-members', EventMemberViewSet,
                base_name='event-members')


urlpatterns = [
    path('', include(router.urls)),
]
