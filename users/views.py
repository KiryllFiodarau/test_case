from django.views.generic import ListView, CreateView, DetailView
from users.forms import UserForm
from users.models import Users
from users.utils import DataMixin


class GetUserByID(DataMixin, DetailView):
    model = Users
    template_name = 'users/user_by_id.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'user'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='GetUserByID')
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = UserForm
    template_name = 'users/register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Register')
        return dict(list(context.items()) + list(c_def.items()))


class GetUsers(DataMixin, ListView):
    model = Users
    template_name = 'users/users.html'
    context_object_name = 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='GetUsers')
        return dict(list(context.items()) + list(c_def.items()))
