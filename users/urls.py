from django.urls import path, include
from .views import authenticate_user, CreateUserAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    # url(r'^create/$', CreateUserAPIView.as_view()),
    path('update/', UserRetrieveUpdateAPIView.as_view()),
    # url(r'^update/$', UserRetrieveUpdateAPIView.as_view()),
    path('obtain_token/', authenticate_user),
    # url(r'^obtain_token/$', authenticate_user),
]
