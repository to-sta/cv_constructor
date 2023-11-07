from django.urls import path

from .views import RegisterNewUserView

app_name = "authentication"

urlpatterns = [path("register/", RegisterNewUserView.as_view(), name="create_user")]
