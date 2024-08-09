from django.views.generic.base import TemplateView
from allauth.account.forms import SignupForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


class home(TemplateView):
    template_name='home.html'


class logoutDashboard(TemplateView):
    template_name = 'account/logout.html'


class SignupView(FormView):
    template_name = 'account/signup.html' # Continua na pagina se obter erro ao ao se registrar
    form_class = SignupForm
    success_url = reverse_lazy('account_login')  # URL para redirecionar após sucesso

    def form_valid(self, form):
        form.save(self.request)  # Salva o usuário no banco de dados
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)