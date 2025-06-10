from django.urls import path
from users.apps import UsersConfig
from users.views import EmailLoginView, LogoutUserView, UserRegistrationView, email_verification, reg_success

app_name = UsersConfig.name



urlpatterns = [
    path('login/', EmailLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutUserView.as_view(template_name='logout.html'), name='logout'),
    path('registration/', UserRegistrationView.as_view(template_name='registration.html'), name='registration'),
    path('users-confirm/<str:token>/', email_verification, name='users-confirm'),
    path('users-success/', reg_success, name='users-success'),
]