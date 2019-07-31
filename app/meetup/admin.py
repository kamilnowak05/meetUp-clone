from django.contrib import admin

from meetup.models import Event, EventCategory, EventReview, EventBooking


admin.site.register(Event)
admin.site.register(EventCategory)
admin.site.register(EventBooking)
admin.site.register(EventReview)