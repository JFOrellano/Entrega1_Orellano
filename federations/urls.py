from django.urls import path

from federations import views

app_name = "federations"

urlpatterns = [
    path("federations", views.federations, name="federations-list"),
    path("federation/add", views.create_federation, name="federation-add"),
]