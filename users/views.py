from django.views.generic import (
    TemplateView,
    ListView,
    FormView,
    CreateView,
    DeleteView,
    View
)
from .forms import OrganizationForm, UserMemberForm
from django.urls import reverse_lazy
from .models import Membership, Organization, UserProfile
from django.shortcuts import get_object_or_404, redirect
from .mixins import AdminOrOwnerMixin
from allauth.account.views import PasswordChangeView


class UserRegistrationView(FormView):
    template_name = "account/signup.html"  
    form_class = OrganizationForm
    success_url = reverse_lazy("account_login")

    def form_valid(self, form):
        form.save(self.request)  # Salva o usuário no banco de dados
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
    

class Home(TemplateView):
    template_name = "dashboard/home.html"
    
    
class Profile(PasswordChangeView):
    template_name = "administration/profile.html"
    
    
class LogoutDashboard(TemplateView):
    template_name = "account/logout.html"


class ListUserView(ListView):
    template_name = "administration/administração_usuarios.html"
    model = Membership
    paginate_by = 20
    
    def get_queryset(self):
        # Obtém a organização do usuário atual
        queryset = super().get_queryset()
        user_memberships = Membership.objects.filter(user=self.request.user)

        # Todas as organizações do usuário
        user_memberships = self.request.user.membership_set.all()
        user_organizations = Organization.objects.filter(
            membership__in=user_memberships
        )

        if user_organizations:
            # Filtra membros com base na organização do usuário atual
            queryset = queryset.filter(organization__in=user_organizations)
        else:
            queryset = queryset.none()

        return queryset.order_by(
            "user__username"
        )  # Retorna uma QuerySet vazia se não houver organização associada

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Adiciona o usuário logado ao contexto
        return context

class CreateUserView(AdminOrOwnerMixin, CreateView):
    model = Membership
    form_class = UserMemberForm
    template_name = "administration/novo_usuario.html"
    success_url = reverse_lazy("user_list_view")
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        # Salva o usuário
        user = form.save(commit=False)
        user.save()

        # Obtém o tipo de permissão selecionado
        type_permission = form.cleaned_data["type_permission"]

        # Obtém a organização do proprietário (usuário logado)
        current_user = self.request.user

        # Certifique-se de que o usuário logado tem uma associação com uma organização
        membership = get_object_or_404(
            Membership, user=current_user, type_permission=Membership.Permission.OWNER
        )
        organization = membership.organization

        # Cria o Membership para o novo usuário
        Membership.objects.create(
            user=user, organization=organization, type_permission=type_permission
        )

        return super().form_valid(form)
    

class EnableUserView(View):
    def get(self, request, *args, **kwargs):
        membership = get_object_or_404(Membership, pk=kwargs['pk'])
        membership.is_active = True
        membership.save()
        return redirect('user_list_view')

class DisableUserView(View):
    def get(self, request, *args, **kwargs):
        membership = get_object_or_404(Membership, pk=kwargs['pk'])
        membership.is_active = False
        membership.save()
        return redirect('user_list_view')


class DeleteUserView(AdminOrOwnerMixin, DeleteView):
    model = Membership
    template_name = "administration/confirm_delete.html"
    success_url = reverse_lazy("user_list_view")
