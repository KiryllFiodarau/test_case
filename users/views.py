from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect

from users.forms import UserForm
from users.models import Users


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('get_users')
            except:
                form.add_error(None, 'Account creation error')
    else:
        form = UserForm()

    return render(request, 'users/register.html', {'form': form})


def get_users_by_id(request, user_id):
    try:
        user = Users.objects.get(pk=user_id)
    except:
        raise Http404()

    return render(request, 'users/user_by_id.html', {'user': user})


def get_users(request):
    user_list = Users.objects.all()
    paginator = Paginator(user_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'users/users.html', {'page_obj': page_obj})
