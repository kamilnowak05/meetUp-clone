from rest_framework import serializers
from groups.models import AppGroup
from django.contrib.auth import get_user_model


User = get_user_model()


class AppGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppGroup
        fields = (
            'id', 'owner', 'name', 'group_category',
            'description', 'group_image', 'member'
            )
        read_only_fields = ('owner', 'member')

    # def create(self, validated_data):
    #     group = AppGroup.objects.create(
    #         owner=self.context['request'].user,
    #         name=validated_data['name'],
    #         description=validated_data['description'],
    #         group_image=validated_data.get('group_image', None)
    #     )
    #     group.group_category.set(validated_data['group_category'])
    #     group.save()
    #     return group


class CreateAppGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppGroup
        fields = (
            'id', 'owner', 'name', 'group_category',
            'description', 'group_image'
            )
        read_only_fields = ('owner', )


class MembersAppGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppGroup
        fields = ('member', )
