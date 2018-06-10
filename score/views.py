from django.shortcuts import render
from .models import KhlTeam, NhlTeam

def home_page(request):
    return render(request, 'score/home_page.html', {})

def khl(request):
    khl_teams = KhlTeam.objects.all()
    return render(request, 'score/khl_page.html', {'khl_teams': khl_teams})

def nhl(request):
    nhl_teams = NhlTeam.objects.all()
    return render(request, 'score/nhl_page.html', {'nhl_teams': nhl_teams})