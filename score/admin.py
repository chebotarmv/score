from django.contrib import admin
from .models import KhlTeam, KhlGame, KhlGameStat, NhlTeam, NhlGame, NhlGameStat

admin.site.register(KhlTeam)
admin.site.register(KhlGame)
admin.site.register(KhlGameStat)
admin.site.register(NhlTeam)
admin.site.register(NhlGame)
admin.site.register(NhlGameStat)
