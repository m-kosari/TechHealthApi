from django.urls import path
from Info.api.view import (
    registration_view,
    Login_view,
    DeleteAccount_view,
    Report_view,
    userInfo_view,
    savePck_view,
    saveStatusUser_view,
    saveStatusGuest_view,
    showPck_view,
    showStatusGuest_view,
    showStatusUser_view,
)

app_name = "Info"

urlpatterns = [
    path('register', registration_view, name="register"),
    path('login', Login_view, name="login"),
    path('delete', DeleteAccount_view, name="delete"),
    path('report', Report_view, name="report"),
    path('user_info', userInfo_view, name="user_info"),
    path('save_pck', savePck_view, name="save_pck"),
    path('status_user', saveStatusUser_view, name="status_user"),
    path('status_guest', saveStatusGuest_view, name="status_guest"),
    path('pck', showPck_view.as_view(),name="pck"),
    path('stsu', showStatusUser_view.as_view(), name="stsu"),
    path('stsg', showStatusGuest_view.as_view(), name="stsg"),
]