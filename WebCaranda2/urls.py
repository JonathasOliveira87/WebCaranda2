from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('contact/', include('contact.urls')),
    path('survey/', include('survey.urls')),
    path('security/', include('security.urls')),
    path('report/', include('report.urls')),
    path('panel/', include('panelUser.urls')),
    path('', auth_views.LoginView.as_view(), name='login'), # usado para redirecionar para o home em caso de nao logado
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)