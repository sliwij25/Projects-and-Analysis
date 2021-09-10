# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 22:23:28 2020

@author: sliwi
"""

import pandas as pd
import numpy as np

# nba api
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import leaguedashplayerbiostats
from nba_api.stats.library.parameters import SeasonAll

player_dict = players.get_players()
jrue = [player for player in player_dict if player ['full_name'] == 'Jrue Holiday'][0]
jrue_id = jrue['id']
print(jrue_id)

bledsoe = [player for player in player_dict if player ['full_name'] == 'Eric Bledsoe'][0]
bledsoe_id = bledsoe['id']
print(bledsoe_id)

from nba_api.stats.endpoints import playercareerstats
# Jrue Holiday
jrue_career = playercareerstats.PlayerCareerStats(player_id='201950')
jrue_career.get_data_frames()[0]

# Eric Bledsoe
bled_career = playercareerstats.PlayerCareerStats(player_id='202339')
bled_career.get_data_frames()[0]