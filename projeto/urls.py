from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static

urlpatterns = [  
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('accounts/', include('allauth.urls')),
    path('users/',include('users.urls')),
    path('tasks/',include('tasks.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)