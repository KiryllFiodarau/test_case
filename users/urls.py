from django.urls import path
from decouple import config
from users.views import GetUsers, GetUserByID, RegisterUser

urlpatterns = [
    path(config('UNIQUE_STR'), RegisterUser.as_view(), name='register'),
    path('api/users/<int:user_id>', GetUserByID.as_view(), name='get_user_by_id'),
    path('api/users/', GetUsers.as_view(), name='get_users'),
]
