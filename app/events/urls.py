from django.urls import path, include

from rest_framework.routers import DefaultRouter

from events.api import views


app_name = 'events'

router = DefaultRouter(trailing_slash=False)
router.register('reviev', views.EventReviewViewSet, basename='reviev')

urlpatterns = [
    path('', include(router.urls)),
    path('list/', views.ListEventView.as_view(), name='list'),
    path('create/', views.CreateEventView.as_view(), name='create'),
    path('manage/<int:event_id>/', views.ManageEventView.as_view(),
         name='manage'),
    path('category/', views.EventCategoryView.as_view(), name='category'),
    path('members/<int:event_id>/', views.EventMemberView.as_view(),
         name='members')
]
