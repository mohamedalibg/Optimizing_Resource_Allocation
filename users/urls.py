
from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, DeleteUserView, SingleUserView, ModifyUserView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('users/', UserView.as_view()),
    path('<int:user_id>/userView/', SingleUserView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('delete/', DeleteUserView.as_view()),
    path('<int:user_id>/modify/', ModifyUserView.as_view())



    

]
