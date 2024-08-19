from django.urls import path

from apps.users.views import UserBlockView, UserListCreateView, UserToAdminView, UserUnblockView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/<int:pk>/block', UserBlockView.as_view()),
    path('/<int:pk>/unblock', UserUnblockView.as_view()),
    path('/<int:pk>/make_admin', UserToAdminView.as_view()),
]
