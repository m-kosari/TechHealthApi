from django.urls import path
from Info.api.view import (
    registration_view,
    Login_view,
)

app_name = "Info"

urlpatterns = [
    path('register' , registration_view , name="register"),
    path('login', Login_view, name="login"),

]