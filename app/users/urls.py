from django.urls import path, include

from rest_framework.routers import DefaultRouter

from users.api import views


app_name = 'users'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', views.UserViewSet, basename='users')

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('', include(router.urls)),
]
