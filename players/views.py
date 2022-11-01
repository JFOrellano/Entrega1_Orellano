from django.shortcuts import render
from django.contrib import messages
from players.models import Player
from players.forms import PlayerForm


# Create your views here.
def players(request):
    players = Player.objects.all()

    context_dict = {"players": players}

    return render(
        request = request,
        context = context_dict,
        template_name="players/players_list.html",
    )

def create_player(request):
    if request.method == "POST":
        player_form = PlayerForm(request.POST)
        if player_form.is_valid():
            data = player_form.cleaned_data
            actual_objects = Player.objects.filter(
                name=data["name"], last_name=data["last_name"], team=data["team"], number=data["number"], position=data["position"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El jugador {data['name']} {data['last_name']} ya existe",
                )
            else:
                player = Player(name=data["name"], last_name=data["last_name"], team=data["team"], number=data["number"], position=data["position"])
                player.save()
                messages.success(
                    request,
                    f"Jugador {data['name']} {data['last_name']} incluido exitosamente!",
                )

            players = Player.objects.all()

            context_dict = {"players": players}

            return render(
                request=request,
                context=context_dict,
                template_name="players/players_list.html",
            )

    player_form = PlayerForm(request.POST)
    context_dict = {"form": player_form}
    return render(
        request=request,
        context=context_dict,
        template_name="players/players_form.html",
    )
