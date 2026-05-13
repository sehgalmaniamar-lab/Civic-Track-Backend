from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
)


class PhoneTokenObtainPairSerializer(
    TokenObtainPairSerializer
):

    username_field = "phone_number"