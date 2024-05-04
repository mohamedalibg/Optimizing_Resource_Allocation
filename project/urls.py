from django.urls import path
from .views import CreateProjectView, RetrieveProjectView, UpdateProjectView, DeleteProjectView

urlpatterns = [
    path('create/', CreateProjectView.as_view()),
    path('<int:pk>/', RetrieveProjectView.as_view()),
    path('<int:pk>/update/', UpdateProjectView.as_view()),
    path('<int:pk>/delete/', DeleteProjectView.as_view()),
]
