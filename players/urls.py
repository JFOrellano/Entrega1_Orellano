from django.urls import path

from players import views

app_name = "players"

urlpatterns = [
    path("players", views.players, name="players-list"),
    path("player/add", views.create_player, name="player-add"),
]