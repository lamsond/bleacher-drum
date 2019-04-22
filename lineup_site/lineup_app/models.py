import django.utils.timezone
from django.db import models

POSITIONS = (
        ('P', 'P'),
        ('C', 'C'),
        ('1B', '1B'),
        ('2B', '2B'),
        ('3B', '3B'),
        ('SS', 'SS'),
        ('LF', 'LF'),
        ('CF', 'CF'),
        ('RF', 'RF'),
        ('DH', 'DH'),
        )

class Team(models.Model):
    location = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=3)

    def __str__(self):
        return self.abbr

class Game(models.Model):
    team_home = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_home')
    team_away = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_away')

    runs_home = models.IntegerField()
    runs_away = models.IntegerField()
    date = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.team_away) + ': ' + str(self.runs_away) + ', ' + str(self.team_home) + ': ' + str(self.runs_home) + ' (' + str(self.date) + ')'

class Player(models.Model):
    name = models.CharField(max_length=100)
    num = models.PositiveSmallIntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return  self.name

class LineupSlot(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    num = models.PositiveSmallIntegerField()
    pos = models.CharField(max_length=2, choices=POSITIONS)
    starter = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return '#' + str(self.player.num) + ' ' + self.player.name + ' (' + self.pos + ')'

