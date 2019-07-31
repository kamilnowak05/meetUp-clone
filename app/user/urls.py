from django.urls import path, include

from rest_framework.routers import DefaultRouter

from user import views


app_name = 'user'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', views.UserViewSet, basename='users')

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('', include(router.urls)),
]
