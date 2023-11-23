from django.urls import path

from .views import UserLoginView, UserLogoutView, UserRegisterView, UserView

app_name = "authentication"

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register-user"),
    path("login/", UserLoginView.as_view(), name="login-user"),
    path("logout/", UserLogoutView.as_view(), name="logout-user"),
    path("user/", UserView.as_view(), name="user"),
]
