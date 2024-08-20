from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.auth.views import ActivateUserView, RecoveryPasswordRequestView, RecoveryPasswordView, SocketView

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
    path('/activate/<str:token>', ActivateUserView.as_view()),
    path('/recovery', RecoveryPasswordRequestView.as_view()),
    path('/recovery/<str:token>', RecoveryPasswordView.as_view()),
    path('/token', SocketView.as_view()),
]
