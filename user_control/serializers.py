from rest_framework import serializers
from .models import CustomUser, Roles, UserActivities


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    fullname = serializers.CharField()
    password = serializers.CharField(required=False)
    role = serializers.ChoiceField(Roles)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(required=False)
    is_new_user = serializers.BooleanField(default=False, required=False)


class UpdatePasswordSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    password = serializers.CharField()


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        exclude = ("password", )


class UserActivitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserActivities
        fields = ("__all__")