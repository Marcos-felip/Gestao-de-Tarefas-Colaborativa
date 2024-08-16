from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Membership

class AdminOrOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        # Verifica se o usuário tem alguma permissão de 'owner' ou 'admin'
        return Membership.objects.filter(user=user, type_permission__in=['owner', 'admin']).exists()
