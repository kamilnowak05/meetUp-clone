from rest_framework import serializers
from .models import Event, EventCategory, EventReview, EventBooking
from user.serializers import UserSerializer


class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = (
            'id', 'category', 'image', 'active'
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
    category_detail = serializers.SerializerMethodField()
    user_detail = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
             'id', 'title', 'about', 'rating',
             'image', 'category',
             'reviews', 'timestamp',
             'user_detail', 'category_detail',
             'location', 'event_date', 'ticket_amount_first',
             'ticket_amount_second', 'event_time_start', 'event_time_end',
             'chief_guest', 'company_name', 'company_phone1', 'company_phone2',
             'company_email', 'company_address', 'company_office',
             'company_web_address', 'approved'
             )
        read_only_fields = ('user', 'rating', 'approved')

    def get_reviews(self, obj):
        reviews = EventReview.objects.filter(event=obj)
        a = []
        for x in reviews:
            review = {}
            review['id'] = x.id
            review['email'] = x.user.email
            review['user'] = x.user.user_id
            review['review'] = x.review
            review['rating'] = x.rating
            review['timestamp'] = x.timestamp
            a.append(review)
        return a

    def get_user_detail(self, obj):
        user_obj = obj.user
        user = UserSerializer(user_obj).data
        return user

    def get_category_detail(self, obj):
        category_obj = obj.category
        category = EventCategorySerializer(category_obj).data
        return category


class EventBookingSerializer(serializers.ModelSerializer):
    event_title = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()

    class Meta:
        model = EventBooking
        fields = (
            'id',
            'user_id',
            'event',
            'event_title',
            'quantity'
        )
        read_only_fields = ('user', 'timestamp')

    def get_id(self, obj):
        return obj.user.id

    def get_event_title(self, obj):
        return obj.event.title


class EventBookingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventBooking
        fields = '__all__'


class ApproveEventSerializer(serializers.ModelSerializer):
    event_title = serializers.SerializerMethodField()
