from django.urls import path, include

from user import views


app_name = 'user'

urlpatterns = [
    path('', views.UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('<int:pk>/', views.UserViewSet.as_view({'get': 'retrieve'}), name='user-pk'),
]
