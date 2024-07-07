from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageTemplateView(TemplateView):
    template_name = 'pages/index.html'


class InstructionTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/instruction.html'
