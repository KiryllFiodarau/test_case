from django.urls import path
from decouple import config
from users import views as user_views

urlpatterns = [
    path(config('UNIQUE_STR'), user_views.register_user, name='register'),
    path('api/users/<int:user_id>', user_views.get_users_by_id, name='get_user_by_id'),
    path('api/users/', user_views.get_users, name='get_users'),
]
