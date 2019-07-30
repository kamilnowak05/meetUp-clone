from django.contrib import admin
from django.contrib.auth.models import Group as Group2

from meetup.models import *
from core.models import UserManager


class group_admin(admin.ModelAdmin):
    list_display = ('name','group_id','creator','category','photo')
    search_fields = ('name','group_id','creator','category')
    list_filter = ('name','group_id','creator','category')
    ordering = ('name',)

admin.site.register(Group,group_admin)


class meetup_admin(admin.ModelAdmin):
    list_display = ('name','meetup_id','host','group','photo','fee','slots')
    search_fields = ('name','meetup_id','host','group')
    list_filter = ('name','meetup_id','host','group')
    ordering = ('name',)

admin.site.register(Meetup,meetup_admin)

admin.site.register(WaitingList)
admin.site.register(Interest)
# admin.site.register(GroupMemberDetails)
# admin.site.register(MeetupMemberDetails)
admin.site.unregister(Group2)