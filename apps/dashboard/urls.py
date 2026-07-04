from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.landing_page_view, name="landing"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("profile/", views.profile_view, name="profile"),
    path("settings/", views.settings_view, name="settings"),
]
