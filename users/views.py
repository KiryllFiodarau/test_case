from django.views.generic import ListView, CreateView, DetailView
from users.forms import UserForm
from users.models import Users

menu = [{'title': "Register", 'url_name': 'register'},
        {'title': "Users", 'url_name': 'get_users'}]


class GetUserByID(DetailView):
    model = Users
    template_name = 'users/user_by_id.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'user'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


class RegisterUser(CreateView):
    form_class = UserForm
    template_name = 'users/register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'User_by_id'
        context['menu'] = menu
        return context


class GetUsers(ListView):
    model = Users
    template_name = 'users/users.html'
    context_object_name = 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Users'
        context['menu'] = menu
        return context
