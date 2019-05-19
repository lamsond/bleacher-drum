import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Game, LineupSlot, Player, Team
from .forms import TeamForm, GameForm

from rest_framework import viewsets
from .serializers import GameSerializer, PlayerSerializer, TeamSerializer

class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows games to be viewed or edited
    """
    queryset = Game.objects.all().order_by('-date')
    serializer_class = GameSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

def play_ball(request):
    return render(request, 'lineup_app/play_ball.html')

def set_lineup(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    nyy = Team.objects.get(abbr='NYY')
    players = Player.objects.filter(team=nyy)
    positions = ('P', 'C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'DH', 'PH')
    slot_indices = range(1, 10)
    context = {'game': game,
            'players': players,
            'positions': positions,
            'slots': slot_indices,
            }

    return render(request, 'lineup_app/set_lineup.html', context)

def save_lineup(request, game_id):
    data = request.POST['hidden']
    if data == '':
        return render(request, 'lineup_app/set_lineup.html', {'error_message': "You didn't set a lineup"})

    data_list = data.split()
    data_strings = json.loads(data_list[0])
    print(data_strings)
    data_dicts = []
    for item in data_strings:
        data_dicts.append(json.loads(item))

    print(data_dicts)

    for lineup_slot in data_dicts:
        game = get_object_or_404(Game, pk=game_id)
        player = get_object_or_404(Player, pk=lineup_slot["player"])
        pos = lineup_slot["pos"]
        slot = lineup_slot["slot"]

        lineup_entry = LineupSlot(game=game, player=player, num=slot, pos=pos,
                starter=0)
        lineup_entry.save()

    return HttpResponseRedirect('/1/set_lineup')

def new_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_game/')
    else:
        form = TeamForm()
    return render(request, 'lineup_app/new_team.html', {'form': form})

def new_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            this_game = form.save()
            game_id = this_game.id
            return HttpResponseRedirect('/' + str(game_id) + '/set_lineup/')
    else:
        form = GameForm()
    return render(request, 'lineup_app/new_game.html', {'form': form})

