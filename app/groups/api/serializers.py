from django.contrib.auth import get_user_model
from groups.models import AppGroup
from rest_framework import serializers

User = get_user_model()


class AppGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppGroup
        fields = ("id", "owner", "name", "group_category", "description", "group_image", "member")
        read_only_fields = ("owner", "member")


class CreateAppGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppGroup
        fields = ("id", "owner", "name", "group_category", "description", "group_image")
        read_only_fields = ("owner",)


class MembersAppGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppGroup
        fields = ("member",)
