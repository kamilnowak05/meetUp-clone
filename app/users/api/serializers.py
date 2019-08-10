from django.contrib.auth import authenticate, get_user_model
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

# User = settings.AUTH_USER_MODEL
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """ Serializers for the user object"""

    class Meta:
        model = User
        fields = (
            'email', 'password', 'first_name',
            'last_name', 'interests'
        )
        read_only_fields = (
            'id', 'last_login', 'is_active', 'user_permissions',
            'is_staff', 'admin'
        )
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """ Create a new user with encrypted password and return it"""
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs