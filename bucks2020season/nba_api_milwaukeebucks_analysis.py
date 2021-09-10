# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 16:29:26 2020

@author: sliwi
"""

import pandas as pd
from nba_api.stats.static import players
player_dict = players.get_players()

giannis = [player for player in player_dict if player ['full_name'] == 'Giannis Antetokounmpo'][0]
giannis_id = giannis['id']

from nba_api.stats.static import teams
team_dict = teams.get_teams()
MIL = [team for team in team_dict if team ['full_name'] == 'Milwaukee Bucks'][0]
MIL_id = MIL['id']

from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll

gamelog_giannis = playergamelog.PlayerGameLog(player_id='203507',season = '2019')
gamelog_giannis_df = gamelog_giannis.get_data_frames()[0]

gamelog_giannis_all = playergamelog.PlayerGameLog(player_id='203507',season = SeasonAll.all)
gamelog_giannis_df_all = gamelog_giannis_all.get_data_frames()[0]

from nba_api.stats.endpoints import leaguegamefinder
MIL_games = leaguegamefinder.LeagueGameFinder(team_id_nullable=MIL_id).get_data_frames()[0]
