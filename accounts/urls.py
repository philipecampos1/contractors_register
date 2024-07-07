from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='account_login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='account_logout'),

    path('accounts/password-change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    path('accounts/password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
    # this part will be asking for email and sending an email
    path('accounts/password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset_form'),
    path('accounts/password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    # this part will be after clicking in the link from the email and changing
    path('accounts/password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

    path('accounts/generate-invitation/', views.GenerateInvitationView.as_view(), name='generate_invitation'),
    path('accounts/invitation-success/', views.InvitationSuccessView.as_view(), name='invitation_success'),
    path('accounts/invitation-fail/', views.InvalidInvitationView.as_view(), name='invalid_invitation'),
    path('accounts/register/<uuid:token>/', views.RegisterView.as_view(), name='register'),
    path('accounts/register-success/', views.RegisterSuccessView.as_view(), name='registration_success')
]
