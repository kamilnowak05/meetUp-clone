from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.api import views

app_name = "users"

router = DefaultRouter(trailing_slash=False)
router.register("", views.UserViewSet, basename="users")

urlpatterns = [
    path("register/", views.CreateUserView.as_view(), name="register"),
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("logout/", views.LogoutUserView.as_view(), name="logout"),
    path("me/", views.ManageUserView.as_view(), name="me"),
    path("", include(router.urls)),
]
