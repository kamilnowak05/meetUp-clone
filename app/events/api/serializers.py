from rest_framework import serializers
from events.models import Event, EventCategory, EventReview
from users.api.serializers import UserSerializer


class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = (
            'id', 'name', 'image'
        )


class EventReviewSerializer(serializers.ModelSerializer):
    user_detail = serializers.SerializerMethodField()
    event_detail = serializers.SerializerMethodField()

    class Meta:
        model = EventReview
        fields = (
            'id',
            'event',
            'rating',
            'timestamp',
            'user_detail',
            'event_detail',
            'review',
        )
        read_only_fields = ('user', )

    def get_user_detail(self, obj):
        return UserSerializer(obj.user).data

    def get_event_detail(self, obj):
        return EventSerializer(obj.event).data


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

#     def get_user(self, obj):
#         return obj.user

#     def get_event_title(self, obj):
#         return obj.event.title

#     def create(self, validated_data):
#         user = validated_data.pop('member', None)
#         eventa = super().create(validated_data)

#         if user:
#             eventa.user.set(user)
#             eventa.save()

#         return eventa


# class EventMemberCreateSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = EventMember
#         fields = '__all__'
