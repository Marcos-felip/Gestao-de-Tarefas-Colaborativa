from django.views.generic import TemplateView, ListView
from allauth.account.forms import SignupForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Membership


class Home(TemplateView):
    template_name='home.html'


class LogoutDashboard(TemplateView):
    template_name = 'account/logout.html'


class Tarefas(TemplateView):
    template_name = 'dashboard/tarefas.html' # redirecionamento para (Tarefas)


class UserManage(ListView):
    template_name = 'account/admistracao_usuarios.html' # redirecionamento para (Admistração de usuario)
    model = Membership
    paginate_by = 20


class SignupView(FormView):
    template_name = 'account/signup.html' # Continua na pagina se obter erro ao ao se registrar
    form_class = SignupForm
    success_url = reverse_lazy('account_login')  # URL para redirecionar após sucesso

    def form_valid(self, form):
        form.save(self.request)  # Salva o usuário no banco de dados
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
    