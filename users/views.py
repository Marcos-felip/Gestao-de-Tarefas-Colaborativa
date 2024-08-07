from django.views.generic.base import TemplateView
from .models import Organization

class home(TemplateView):
    template_name='base.html'

class logoutDashboard(TemplateView):
    template_name = 'account/logout.html'

