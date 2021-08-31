from decouple import config

menu = [{'title': "Register", 'url_name': 'register'},
        {'title': "Users", 'url_name': 'get_users'}]


class DataMixin:
    paginate_by = config('PAGE_COUNT')

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
