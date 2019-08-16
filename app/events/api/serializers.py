from rest_framework import serializers
from events.models import Event, EventCategory, EventReview


class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = (
            'id', 'name', 'image'
        )


class EventReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventReview
        fields = (
            'id',
            'event',
            'user',
            'rating',
            'timestamp',
            'review',
        )
        read_only_fields = ('user', )


class EventSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'id', 'owner_group', 'title', 'about',
            'rating', 'image', 'category', 'reviews', 'timestamp',
            'location', 'event_date', 'event_time_start',
            'event_time_end', 'chief_guest', 'member'
        )
        read_only_fields = ('id', 'rating', 'member')

    def get_reviews(self, obj):
        reviews = EventReview.objects.filter(event=obj)
        a = []
        for x in reviews:
            review = {}
            review['id'] = x.id
            review['email'] = x.user.email
            review['user'] = x.user.id
            review['review'] = x.review
            review['rating'] = x.rating
            review['timestamp'] = x.timestamp
            a.append(review)
        return a


class CreateEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            'id', 'owner_group', 'title', 'about',
            'image', 'category', 'timestamp',
            'location', 'event_date', 'event_time_start',
            'event_time_end', 'chief_guest'
        )
        read_only_fields = ('id', 'owner_group', )


class EventMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'member', 'title')
        read_only_fields = ('id', 'title')
