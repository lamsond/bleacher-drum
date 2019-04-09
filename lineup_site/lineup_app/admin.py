from django.contrib import admin
from .models import Team, Player, LineupSlot, Game

# Register your models here.
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(LineupSlot)
admin.site.register(Game)

