from django.urls import path, include

from meetup.views import ApproveEvent, EventViewSet, EventCategoryViewSet, EventReviewViewSet, EventBookingViewSet

from rest_framework.routers import DefaultRouter


app_name = 'meetup'

router = DefaultRouter()
router.register(r'events', EventViewSet, base_name='events')
router.register(r'event-category', EventCategoryViewSet,
                base_name='event-category')
router.register(r'event-review', EventReviewViewSet, base_name='event-review')
router.register(r'event-booking', EventBookingViewSet,
                base_name='event-booking')


urlpatterns = [
    path('', include(router.urls)),
    path('approve/', ApproveEvent.as_view(), name='approve'),
]
