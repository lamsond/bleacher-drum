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

@login_required
def set_lineup(request, game_id, ctx):
    game = get_object_or_404(Game, pk=game_id)
    if ctx == 'away':
        players = Player.objects.filter(team=game.team_away)
    else:
        players = Player.objects.filter(team=game.team_home)
    positions = ('P', 'C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'DH', 'PH')
    slot_indices = range(1, 10)
    context = {'game': game,
            'players': players,
            'positions': positions,
            'slots': slot_indices,
            'ctx': ctx,
            }

    return render(request, 'lineup_app/set_lineup.html', context)

@login_required
def set_pitchers(request, game_id, ctx):
    game = Game.objects.get(pk=game_id)
    if ctx == 'away':
        players = Player.objects.filter(team=game.team_away)
    else:
        players = Player.objects.filter(team=game.team_home)
    slot_indices = range(1, 13)

    context = {'game': game,
            'players': players,
            'slots': slot_indices,
            'ctx': ctx,
            }

    return render(request, 'lineup_app/set_pitchers.html', context)

@login_required
def save_lineup(request, game_id, ctx):
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

        if pitchers:
            lineup_entry = LineupSlot(game=game, player=player, num=10, pos=pos, starter=int(slot)-1)
            query = LineupSlot.objects.filter(game=game).filter(num=10).filter(starter=int(slot)-1).filter(player__team=player.team)
            if len(query) == 1:
                print("deleting: " + str(query))
                query[0].delete()
        else:
            lineup_entry = LineupSlot(game=game, player=player, num=slot, pos=pos, starter=0)
            query = LineupSlot.objects.filter(game=game).filter(num=slot).filter(starter=0).filter(player__team=player.team)
            if len(query) == 1:
                print("deleting: " + str(query))
                query[0].delete()
        lineup_entry.save()
        url = ''
        if pitchers:
            if ctx == 'home':
                url = '/' + str(game_id) + '/view_lineup/'
            elif ctx == 'away':
                url = '/' + str(game_id) + '/set_pitchers/home/'
        else:
            if ctx == 'away':
                url = '../../set_lineup/home/'
            elif ctx == 'home':
                url = '/' + str(game_id) + '/set_pitchers/away/'

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
        return HttpResponseRedirect('/new_player/')

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
            return HttpResponseRedirect('/' + str(game_id) + '/set_lineup/away/')
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
def view_team(request, team_id):
    team = Team.objects.get(pk=team_id)
    players = Player.objects.filter(team=team)
    context = {'team': team, 'players': players}
    return render(request, 'lineup_app/view_team.html', context)

@login_required
def view_players(request):
    players = Player.objects.filter(owner=request.user).order_by('team').all()
    context = {'players': players}
    return render(request, 'lineup_app/view_players.html', context)

@login_required
def view_player(request, player_id):
    context = {'player': Player.objects.get(pk=player_id)}
    return render(request, 'lineup_app/view_player.html', context)

@login_required
def view_lineup(request, game_id):
    game = Game.objects.get(pk=game_id)
    at = game.team_away
    ht = game.team_home
    awayslots = LineupSlot.objects.filter(game=game).filter(player__team=at).filter(starter=0).order_by('num')
    homeslots = LineupSlot.objects.filter(game=game).filter(player__team=ht).filter(starter=0).order_by('num')
    context = {'awayslots': awayslots, 'homeslots': homeslots, 'game': game}
    return render(request, 'lineup_app/view_lineup.html', context)