from rest_framework import serializers
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView
from .models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.hashers import make_password


class UserOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "full_name",
            "city",
            "state",
            "gender",
            "sector",
            "last_login",
            "date_joined",
        ]


class UserInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "email",
            "full_name",
            "city",
            "state",
            "gender",
            "sector",
        ]


class MultiSerializerModelView(object):
    serializers = {}

    def get_serializer_class(self):
        action = self.request.method.lower()
        return self.serializers.get(action, self.serializer_class)


class UsersMeView(
    MultiSerializerModelView,
    UpdateAPIView,
    RetrieveUpdateAPIView
):
    queryset = User.objects.all()
    serializer_class = UserOutputSerializer
    permission_classes = [IsAuthenticated]
    serializers = {
        'retrieve': UserOutputSerializer,
        'update': UserInputSerializer,
        'partial_update': UserInputSerializer,
    }

    def get_object(self):
        return self.request.user


class UserCreateInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "full_name",
            "city",
            "state",
            "gender",
            "sector",
        ]

        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
        }

    def validate_password(self, value: str) -> str:
        return make_password(value)


class UsersView(CreateAPIView):
    authentication_classes = []
    serializer_class = UserCreateInputSerializer
