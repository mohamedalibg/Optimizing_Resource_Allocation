
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('engineers/', include('resource.urls')),
    path('projects/', include('project.urls')),
    path('dashboard/', include('dashboard.urls'))





]
