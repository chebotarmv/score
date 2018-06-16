# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home', views.home_page, name='home_page'),
    url(r'^khl', views.khl, name='khl'),
    url(r'^nhl', views.nhl, name='nhl'),
    url(r'^archivekhl', views.khl_archive, name='khl_archive'),
    url(r'^archivenhl', views.khl_archive, name='nhl_archive')
]
"""


url(r'home/khl/team', views.khl_team, name='khl_team'),
url(r'home/nhl/team', views.nhl_team, name='nhl_team'),
url(r'home/khl/gamestat', views.khl_gamestat, name='khl_gamestat'),
url(r'home/nhl/gamestat', views.nhl_gamestat, name='nhl_gamestat'),
url(r'home/khl/archive', views.khl_archive, name='khl_archive'),
url(r'home/nhl/archive', views.nhl_archive, name='nhl_archive'),
url(r'home/makedata', views.makedata, name='make_data'),
url(r'datacheck', views.datacheck, name='data_check')"""