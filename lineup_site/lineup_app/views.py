from django.shortcuts import render
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
    return HttpResponse("<h1>Coming soon...</h1>")

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
            form.save()
            return HttpResponseRedirect('/play_ball/')
    else:
        form = GameForm()
    return render(request, 'lineup_app/new_game.html', {'form': form})

