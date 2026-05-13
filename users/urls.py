from django.urls import path

from .views import SignupView

from .views import (
    SignupView,
    PhoneLoginView,
)


urlpatterns = [
    path(
        "signup/",
        SignupView.as_view(),
    ),

    path(
        "login/",
        PhoneLoginView.as_view(),
    ),
]