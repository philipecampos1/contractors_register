from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from .forms import InvitationForm, CustomUserCreationForm
from .models import Invitation
from django.shortcuts import redirect
from django.views.generic import TemplateView


class GenerateInvitationView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'accounts/generate_invation.html'
    form_class = InvitationForm
    success_url = reverse_lazy('invitation_success')

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        invitation = form.save(commit=False)
        invitation.group = form.cleaned_data['group']
        invitation.save()

        invite_url = self.request.build_absolute_uri(reverse_lazy('register', kwargs={'token': invitation.token}))
        superuser_email = self.request.user.email
        send_mail(
            'You are invited to join the platform contractors register',
            f'Click the link to register: {invite_url}',
            superuser_email,
            [invitation.email]
        )
        return super().form_valid(form)


class InvitationSuccessView(TemplateView):
    template_name = 'accounts/invitation_success.html'


class InvalidInvitationView(TemplateView):
    template_name = 'accounts/invalid_invitation.html'


class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('registration_success')

    def dispatch(self, request, *args, **kwargs):
        token = kwargs.get('token')
        if token is None:
            return redirect('invalid_invitation')

        try:
            self.invitation = Invitation.objects.get(token=token, is_used=False)
        except Invitation.DoesNotExist:
            return redirect('invalid_invitation')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if not hasattr(self, 'invitation'):
            return redirect('invalid_invitation')

        user = form.save(commit=False)
        user.email = self.invitation.email
        user.save()

        user.groups.add(self.invitation.group)

        self.invitation.is_used = True
        self.invitation.save()

        return super().form_valid(form)


class RegisterSuccessView(TemplateView):
    template_name = 'accounts/register_success.html'
