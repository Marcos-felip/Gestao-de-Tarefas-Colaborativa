from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from .models import Organization


class home(TemplateView):
    template_name='base.html'

@login_required
def user_profile_view(request):
    user = request.user
    organization = Organization.objects.filter(owner=user).first()
    return render(request, 'profile.html', {'organization': organization})