menu = [{'title': "Register", 'url_name': 'register'},
        {'title': "Users", 'url_name': 'get_users'}]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
