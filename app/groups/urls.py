from django.urls import path

from groups.api import views


app_name = 'groups'


urlpatterns = [
    path('list/', views.ListAppGroupView.as_view(), name='list'),
    #     path('list/<int:group_id>', views.ListAppGroupView.as_view(),
    #          name='group'),
    path('create/', views.CreateAppGroupView.as_view(), name='create'),
    path('manage/<int:group_id>/', views.ManageAppGroupView.as_view(),
         name='manage'),
    path('members/<int:group_id>/', views.MembersAppGroupView.as_view(),
         name='members')
]
