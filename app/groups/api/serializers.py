from rest_framework import serializers
from groups.models import AppGroup


class AppGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppGroup
        fields = ('owner', 'name', 'description', 'members', 'group_image')