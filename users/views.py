from django.views.generic import TemplateView, ListView, CreateView, DeleteView 
from allauth.account.forms import SignupForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Membership, Organization


class Home(TemplateView):
    template_name='home.html'


class LogoutDashboard(TemplateView):
    template_name = 'account/logout.html'


class CreateUser(TemplateView):
    template_name = 'administration/novo_usuario.html'


class Tasks(TemplateView):
    template_name = 'dashboard/tasks.html' # redirecionamento para (Tarefas)


class ListUserView(ListView):
    template_name = 'administration/administração_usuarios.html' # redirecionamento para (Admistração de usuario)
    model = Membership
    paginate_by = 20
    context_object_name = 'usuarios'

    def get_queryset(self):
        # Obtém a organização do usuário atual
        user_memberships = Membership.objects.filter(user=self.request.user)

        #todas as organizações do usuário
        user_memberships = self.request.user.membership_set.all()

        user_organizations = Organization.objects.filter(membership__in=user_memberships)

        if user_organizations:
            # Filtra membros com base na organização do usuário atual
            queryset = Membership.objects.filter(organization__in=user_organizations)
            
        return queryset # Retorna uma QuerySet vazia se não houver organização associada


class CreateUserView(CreateUser):
    model = Membership
    


class SignupView(FormView):
    template_name = 'account/signup.html' # Continua na pagina se obter erro ao ao se registrar
    form_class = SignupForm
    success_url = reverse_lazy('account_login')  # URL para redirecionar após sucesso

    def form_valid(self, form):
        form.save(self.request)  # Salva o usuário no banco de dados
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
    