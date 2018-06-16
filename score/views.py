from django.shortcuts import render
from .models import KhlTeam, NhlTeam, KhlGame, NhlGame
import datetime

def home_page(request):
    return render(request, 'score/home_page.html', {})

def khl(request):
    khl_teams = KhlTeam.objects.all()
    return render(request, 'score/khl_page.html', {'khl_teams': khl_teams})

def nhl(request):
    nhl_teams = NhlTeam.objects.all()
    return render(request, 'score/nhl_page.html', {'nhl_teams': nhl_teams})

def khl_archive(request):
    get_khlgame_obj = KhlGame.objects.all().values()
    data = get_khlgame_obj[0:]
    return render(request, 'score/khl_archive.html', context={'data':data})

def nhl_archive(request):
    get_nhlgame_obj = NhlGame.objects.all().values()
    data = get_nhlgame_obj[0:]
    return render(request, 'score/khl_archive.html', context={'data':data})
