from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    path("", views.blogs_list_view, name="list"),
    path("favorites/", views.favorites_view, name="favorites"),
    path("history/", views.history_view, name="history"),
    path("<slug:slug>/", views.blog_detail_view, name="detail"),
]
