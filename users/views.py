import secrets
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from .forms import UserForm, UserRegistrationForm
from .models import User


def reg_success(request):
    return render(request, 'users_confirm.html')


class EmailLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = UserForm


class LogoutUserView(LogoutView):
    template_name = 'users/logout.html'


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:users-success')

    def form_valid(self, form):
        user = form.save()
        user.is_active =False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/users-confirm/{token}'

        send_mail(
            subject='Подтверждение регистрации',
            message=f'Для подтверждения регистрации перейдите по ссылке: \n{url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],)

        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))