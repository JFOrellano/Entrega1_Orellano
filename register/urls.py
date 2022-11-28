from django.urls import path

from register import views

app_name = "register"

urlpatterns = [
    path("register", views.register, name="registro"),
    ]