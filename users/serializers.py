from rest_framework import serializers

from .models import User


class SignupSerializer(
    serializers.ModelSerializer
):

    password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User

        fields = [
            "phone_number",
            "password",
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            phone_number=validated_data[
                "phone_number"
            ],

            password=validated_data[
                "password"
            ],
        )

        return user