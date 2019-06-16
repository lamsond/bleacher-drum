import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Game, LineupSlot, Player, Team
from .forms import TeamForm, GameForm

def index(request):
    return render(request, 'lineup_app/index.html')

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid:
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect('/')
    
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def play_ball(request):
    return render(request, 'lineup_app/play_ball.html')

@login_required
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

@login_required
def set_pitchers(request, game_id):
    game = Game.objects.get(pk=game_id)
    nyy = Team.objects.get(abbr='NYY')
    players = Player.objects.filter(team=nyy)
    slot_indices = range(1, 13)

    context = {'game': game,
            'players': players,
            'slots': slot_indices,
            }

    return render(request, 'lineup_app/set_pitchers.html', context)

@login_required
def save_lineup(request, game_id):
    pitchers = True
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
        if pos != 'P':
            pitchers = False
        slot = lineup_slot["slot"]

        lineup_entry = LineupSlot(game=game, player=player, num=10, pos=pos,
                starter=int(slot)-1)
        lineup_entry.save()
        url = '/' + str(game_id) + '/set_pitchers/'
        if pitchers:
            url = '/new_game/'
    return HttpResponseRedirect(url)

@login_required
def new_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            new_team = form.save(commit=False)
            new_team.owner = request.user
            new_team.save()
            return HttpResponseRedirect('/new_game/')
    else:
        form = TeamForm()
    return render(request, 'lineup_app/new_team.html', {'form': form})
@login_required
def new_player(request):
    if request.method == 'POST':
        name = request.POST['player_name']
        num = int(request.POST['player_num'])
        team = Team.objects.get(abbr=request.POST['team'])
        owner = request.user
        new_player = Player(name=name, num=num, team=team, owner=owner)
        new_player.save()
        return HttpResponseRedirect('/')

    teams = Team.objects.filter(owner=request.user).all()
    context = {'teams': teams}
    return render(request, 'lineup_app/new_player.html', context)


@login_required
def new_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            this_game = form.save(commit=False)
            this_game.owner = request.user
            this_game.save()
            game_id = this_game.id
            return HttpResponseRedirect('/' + str(game_id) + '/set_lineup/')
    else:
        form = GameForm()
        form.fields['team_home'].queryset = Team.objects.filter(owner=request.user)
        form.fields['team_away'].queryset = Team.objects.filter(owner=request.user)
    return render(request, 'lineup_app/new_game.html', {'form': form})


@login_required
def view_games(request):
    games = Game.objects.filter(owner=request.user).order_by('-date').all()
    context = {'games': games}
    return render(request, 'lineup_app/view_games.html', context)

@login_required
def view_teams(request):
    teams = Team.objects.filter(owner=request.user).order_by('abbr').all()
    context = {'teams': teams}
    return render(request, 'lineup_app/view_teams.html', context)

@login_required
def view_players(request):
    players = Player.objects.filter(owner=request.user).order_by('team').all()
    context = {'players': players}
    return render(request, 'lineup_app/view_players.html', context)

