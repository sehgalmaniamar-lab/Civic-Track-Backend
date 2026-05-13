from rest_framework import generics

from .models import User
from .serializers import SignupSerializer

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from .jwt_serializer import (
    PhoneTokenObtainPairSerializer,
)

class SignupView(
    generics.CreateAPIView
):

    queryset = User.objects.all()

    serializer_class = SignupSerializer




class PhoneLoginView(
    TokenObtainPairView
):

    serializer_class = (
        PhoneTokenObtainPairSerializer
    )