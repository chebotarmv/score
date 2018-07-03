# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import KhlTeam, NhlTeam, KhlGame, NhlGame, KhlGameStat
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from score.forms import *




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

def makekhldata(request):
    khlform = KhlGameForm()
    return render(request, "score/make_khl_data.html", {"form": khlform})

def makenhldata(request):
    nhlform = NhlGameForm()
    return render(request, "score/make_nhl_data.html", {"form": nhlform})

def teamstat(request, name):
    last_game = KhlGameStat.objects.filter(team_name_id='name').values()[:3]
    get_first_period_stat = last_game[0]
    first_period_shots = get_first_period_stat['shot_count']
    first_period_reflected = get_first_period_stat['reflected_count']
    get_second_period_stat = last_game[1]
    second_period_shots = get_second_period_stat['shot_count']
    second_period_reflected = get_second_period_stat['reflected_count']
    get_third_period_stat = last_game[2]
    third_period_shots = get_third_period_stat['shot_count']
    third_period_reflected = get_third_period_stat['reflected_count']
    last_five_game = KhlGameStat.objects.filter(team_name_id='name').values()[:15]
    #five_period_shots =

