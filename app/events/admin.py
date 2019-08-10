from django.contrib import admin

from .models import Event, EventCategory, EventReview, EventMember


admin.site.register(Event)
admin.site.register(EventCategory)
admin.site.register(EventMember)
admin.site.register(EventReview)
