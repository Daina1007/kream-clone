from django.urls import path
from . import views

app_name = "style"

urlpatterns = [
    path("", views.StyleListView.as_view(), name="list"),
]
