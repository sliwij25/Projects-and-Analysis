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

import matplotlib.pyplot as plt
import seaborn as sns

# import shape of court
from matplotlib import cm
from matplotlib.patches import Circle, Rectangle, Arc, ConnectionPatch
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import LinearSegmentedColormap, ListedColormap, BoundaryNorm
from matplotlib.path import Path
from matplotlib.patches import PathPatch

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
    return shotchartlist[0], shotchartlist[1]
   

# draw court function

def draw_court(ax=None, color="blue", lw=1, outer_lines=False):
    
    if ax is None:
        ax = plt.gca()
        
    # basketball hoop
    hoop = Circle((0,0), radius=7.5, linewidth=lw, color=color, fill=False)
    
    # backboard
    backboard = Rectangle((-30, -12.5), 60, 0, linewidth=lw, color=color)
    
    # the paint
    outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color, fill=False)
    inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color, fill=False)
    
    # free throw top arc
    top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180, linewidth=lw, color=color, fill=False)
    
    # free throw bottom arc
    bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0, linewidth=lw, color=color)
    
    # restricted zone
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw, color=color)
    
    # three point line
    corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw, color=color)
    corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color)
    three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw, color=color)
    
    # center court
    center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0, linewidth=lw, color=color)
    center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0, linewidth=lw, color=color)
    
    court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw, bottom_free_throw, restricted,
                      corner_three_a, corner_three_b, three_arc, center_outer_arc, center_inner_arc]
    
    outer_lines=True
    if outer_lines:
        outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=lw, color=color, fill=False)
        court_elements.append(outer_lines)
    
    for element in court_elements:
        ax.add_patch(element)
        
# shot chart function
def shot_chart(data, title="", color="b", xlim=(-250, 250), ylim=(422.5, -47.5), line_color="blue",
               court_color="white", court_lw=2, outer_lines=False,
               flip_court=False, gridsize=None,
               ax=None, despine=False):
    
    if ax is None:
        ax = plt.gca()
        
    if not flip_court:
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
    else:
        ax.set_xlim(xlim[::-1])
        ax.set_ylim(ylim[::-1])
    
    ax.tick_params(labelbottom="off", labelleft="off")
    ax.set_title(title, fontsize=18)
    
    # draws the court using the draw_court()
    draw_court(ax, color=line_color, lw=court_lw, outer_lines=outer_lines)
    
    # separate color by make or miss
    x_missed = data[data['EVENT_TYPE'] == 'Missed Shot']['LOC_X']
    y_missed = data[data['EVENT_TYPE'] == 'Missed Shot']['LOC_Y']
    
    x_made = data[data['EVENT_TYPE'] == 'Made Shot']['LOC_X']
    y_made = data[data['EVENT_TYPE'] == 'Made Shot']['LOC_Y']
    
    # plot missed shots
    ax.scatter(x_missed, y_missed, c='r', marker="x", s=100, linewidths=3)
    # plot made shots
    ax.scatter(x_made, y_made, facecolors='none', edgecolors='g', marker="o", s=100, linewidths=3)
    
    # set the spines to match rest of court, makes outer_lines
    for spine in ax.spines:
        ax.spines[spine].set_lw(court_lw)
        ax.spines[spine].set_color(line_color)
    
    if despine:
        ax.spines["top"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
    
    return ax
    

if __name__ == "__main__":
    player_shotchart_df, league_avg = get_player_shotchartdetail("Jrue Holiday", "2019-20")
  
    shot_chart(player_shotchart_df, title="Jrue Holiday Shot Chart 2019-20")
    # set size for plots
    plt.rcParams['figure.figsize'] = (12, 11)
    plt.show()
    
if __name__ == "__main__":
    player_shotchart_df, league_avg = get_player_shotchartdetail("Eric Bledsoe", "2019-20")
  
    shot_chart(player_shotchart_df, title="Eric Bledsoe Shot Chart 2019-20")
    # set size for plots
    plt.rcParams['figure.figsize'] = (12, 11)
    plt.show()