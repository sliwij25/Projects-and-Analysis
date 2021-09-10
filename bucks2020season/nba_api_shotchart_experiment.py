# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 16:46:51 2020

@author: sliwi
"""

import pandas as pd
import numpy as np

# nba api
from nba_api.stats.static import players
from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.endpoints import playercareerstats

# get player shot chart detail
def get_player_shotchartdetail(player_name, season_id):
    
    # player dictionary
    nba_players = players.get_players()
    player_dict = [player for player in nba_players if player ['full_name'] == player_name][0]
    print(player_dict)

    # career dataframe
    career = playercareerstats.PlayerCareerStats(player_id=player_dict['id'])
    career_df = career.get_data_frames()[0]
    print(career_df)
    
    # team id during season
    team_id = career_df[career_df['SEASON_ID'] == season_id]['TEAM_ID']
    print(team_id)
    
    # shotchartdetail
    shotchartlist = shotchartdetail.ShotChartDetail(team_id=int(team_id),
                                                    player_id=int(player_dict['id']),
                                                    season_type_all_star='Regular Season',
                                                    season_nullable=season_id,
                                                    context_measure_simple="FGA").get_data_frames()
    print(shotchartlist)
   


if __name__ == "__main__":
    get_player_shotchartdetail("Jrue Holiday", "2019-20")
    
