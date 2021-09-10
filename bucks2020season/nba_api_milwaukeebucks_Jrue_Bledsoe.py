# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:36:52 2020

@author: sliwi
"""

import pandas as pd

# nba api
from nba_api.stats.static import teams
from nba_api.stats.endpoints import cumestatsteam
from nba_api.stats.endpoints import cumestatsplayer

team_dict = teams.get_teams()
MIL = [team for team in team_dict if team ['full_name'] == 'Milwaukee Bucks'][0]
MIL_id = MIL['id']
