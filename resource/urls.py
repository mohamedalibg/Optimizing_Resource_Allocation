from django.urls import path
from .views import AddEngineerView, DeleteEngineerView, ViewAllEngineersView, ViewEngineerDetailsView, ModifyEngineerDetailsView

urlpatterns = [
    path('add/', AddEngineerView.as_view()),
    path('<int:pk>/delete/', DeleteEngineerView.as_view()),
    path('all/', ViewAllEngineersView.as_view()),
    path('<int:pk>/', ViewEngineerDetailsView.as_view()),
    path('<int:pk>/modify/', ModifyEngineerDetailsView.as_view()),
]
