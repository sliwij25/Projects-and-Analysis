# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:17:23 2020

@author: sliwi
"""

import pandas as pd
import numpy as np

# nba api
from nba_api.stats.static import players
from nba_api.stats.endpoints import cumestatsplayer
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll

player_dict = players.get_players()
jrue = [player for player in player_dict if player ['full_name'] == 'Jrue Holiday'][0]
jrue_id = jrue['id']
print(jrue_id)

bledsoe = [player for player in player_dict if player ['full_name'] == 'Eric Bledsoe'][0]
bledsoe_id = bledsoe['id']
print(bledsoe_id)

# Jrue Holiday
season = cumestatsplayer.TotalPlayerStats(player_id='201950')
season.get_data_frames()[0]

# Eric Bledsoe
season = cumestatsplayer.TotalPlayerStats(player_id='202339')
season.get_data_frames()[0]





# get player stats detail
def get_player_cumestatsplayer(player_name, season_id):

# jrue stats 2019 season
    def get_player_cumestatsplayer('Jrue Holiday', 2019): "TotalPlayerStats": ["DISPLAY_FI_LAST","PERSON_ID","GP", "GS", "ACTUAL_MINUTES", "ACTUAL_SECONDS", "FG",
            "FGA", "FG_PCT", "FG3", "FG3A", "FG3_PCT", "FT", "FTA", "FT_PCT", "OFF_REB", "DEF_REB", "TOT_REB",
            "AST", "PF", "STL", "TURNOVERS", "BLK", "PTS", "MAX_ACTUAL_MINUTES", "MAX_ACTUAL_SECONDS",
            "MAX_REB", "MAX_AST", "MAX_STL", "MAX_TURNOVERS", "MAX_BLK", "MAX_PTS", "AVG_ACTUAL_MINUTES",
            "AVG_ACTUAL_SECONDS", "AVG_TOT_REB", "AVG_AST", "AVG_STL", "AVG_TURNOVERS", "AVG_BLK",
            "AVG_PTS", "PER_MIN_TOT_REB", "PER_MIN_AST", "PER_MIN_STL", "PER_MIN_TURNOVERS",
            "PER_MIN_BLK", "PER_MIN_PTS"]

# bledsoe stats 2019 season
def get_player_cumestatsplayer('Eric Bledsoe', 2019): "TotalPlayerStats": ["DISPLAY_FI_LAST", "PERSON_ID","GP", "GS", "ACTUAL_MINUTES", "ACTUAL_SECONDS", "FG",
            "FGA", "FG_PCT", "FG3", "FG3A", "FG3_PCT", "FT", "FTA", "FT_PCT", "OFF_REB", "DEF_REB", "TOT_REB",
            "AST", "PF", "STL", "TURNOVERS", "BLK", "PTS", "MAX_ACTUAL_MINUTES", "MAX_ACTUAL_SECONDS",
            "MAX_REB", "MAX_AST", "MAX_STL", "MAX_TURNOVERS", "MAX_BLK", "MAX_PTS", "AVG_ACTUAL_MINUTES",
            "AVG_ACTUAL_SECONDS", "AVG_TOT_REB", "AVG_AST", "AVG_STL", "AVG_TURNOVERS", "AVG_BLK",
            "AVG_PTS", "PER_MIN_TOT_REB", "PER_MIN_AST", "PER_MIN_STL", "PER_MIN_TURNOVERS",
            "PER_MIN_BLK", "PER_MIN_PTS"]