from django.contrib import admin
from .models import UserProfile
from .models import Organization
admin.site.register(UserProfile)
admin.site.register(Organization)
