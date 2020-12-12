#!/usr/bin/env python
# coding: utf-8

# # # Analysis of the Milwaukee Bucks 2019-20 season and the impact of Giannis

# ![Image of Giannis](data:image/jpeg;base64,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)

# For my first basketball python project, I will dive into analyzing the Milwaukee Bucks 2019-20 season along with Giannis Antetokounmpo's impact on the season. I will be using the 2019-20 Milwaukee Bucks Stats from Basketball Reference, specifically the Totals table. You can find this: https://www.basketball-reference.com/teams/MIL/2020.html
# 
# The analyzation will be simple to lay the foundation for building my python knowledge base and skillset. It will include data strictly from the 2019-20 season. The steps include:
# 1. computing the average age of the Bucks roster
# 2. calculating the percentage of the team's points, assists, and rebounds that Giannis Antetokounmpo accounted for
# 3. creating a new data frame consisting of the average points, assists, and rebounds per game played of everyone on the roster
# 
# For this analysis, I will need the following packages:

# In[1]:


import pandas as pd
import numpy as np


# My first step will be to load the data that I extracted from Basketball Reference. To preface column header meanings are as follow:
# GP = Games Played
# GS = Games Started
# MP = Minutes Played
# TRB = Total Rebounds (Defensive and Offensive)
# AST = Assists
# STL = Steals
# BLK = Blocks
# PTS = Points

# In[4]:


#importing csv of 2019-20 Milwaukee Bucks player totals
bucks = pd.read_csv (r'C:\Users\sliwi\OneDrive\Documents\Colding\HoopsData\Projects\bucks2020season\Bucks 2019-20 totals.csv')
bucks


# After pulling in the raw data, the first data segment that stands out is age. With the Bucks being in title contention, having veterans on their roster is key. I suspect that the age of the players will be relatively old. I will now find out the Bucks average age of their roster.

# In[5]:


# average age of Bucks players rounded to the nearest tenth
averageage = bucks['Age'].mean()
round(averageage, 1)


# An average age of 28.5 seems relatively old for a roster. To put that into perspective, this would be in the top 5 oldest rosters in the NBA during the 2019-20 season. The Houston Rockets had the oldest roster averaging an age of 30.2 per player, while the Phoenix Suns were the youngest at 24.4 per Lineups.com/nba/rosters.
# 
# My next step is to find the total points, assists, and rebounds accumulated by the roster. This will help me with my final analysis of finding the percentage of points, assists, and rebounds that Giannis accounted for.

# In[6]:


pts_total = bucks['PTS'].sum()
ast_total = bucks['AST'].sum()
trb_total = bucks['TRB'].sum()


# In[7]:


# Bucks point total for 2019-20 season
pts_total


# In[8]:


# Bucks assist total for 2019-20 season
ast_total


# In[9]:


# Bucks rebound total for 2019-20 season
trb_total


# Now that I have the total points, assists, and rebounds, I will dive into finding the impact Giannis had on this team. Below you will see just data from Giannis. If you did not notice, Giannis led the team in total points, assists and rebounds, quite an accomplishment and fitting for his unicorn status.

# In[10]:


# show 1st row of data frame (Giannis)
bucks.iloc[:1]


# I can now use the total points, assists, and rebounds from the team that I calculated earlier. The first equation will be for finding the percent of the Bucks points that Giannis scored.

# In[11]:


# percent of Bucks 2019-20 total points scored from Giannis
round(1857/8663*100, 2)


# Next is finding the percent of Bucks assists that Giannis accounted for.

# In[12]:


# percent of Bucks 2019-20 total assists from Giannis
round(354/1889*100, 2)


# Lastly, I will calculate the percent of Bucks rebounds that Giannis had.

# In[13]:


# percent of Bucks 2019-20 total rebounds from Giannis
round(856/3774*100, 2)


# Without diving into how Giannis ranks across the league in these categories, it is simply impressive that he led his team in all three categories.
# 
# For Giannis not being a shooter, he led the team in points showing his dominance in the paint.
# 
# For Giannis not being the team's point guard, he led the team in assists showing his playmaking ability.
# 
# For Giannis not being the team's center, he led the team in rebounds showing his ability to control the glass.
# 
# Giannis nearly accounts for 20% of the team's status for points, assists, and rebounds. This analysis showcases the massive dependence that the Bucks have for Giannis.

# The final part of my project includes creating a new data frame of the players on the roster and each of their average points per game, assists per game, and rebounds per game.

# In[14]:


pergame = pd.DataFrame(bucks, columns = ['Player']) 
pergame


# In[15]:


# ppg = points per game
PTS_GP = bucks['PTS']/bucks['GP']
pergame.insert(1, 'ppg', PTS_GP, True)
pergame


# In[16]:


# apg = assists per game
AST_GP = bucks['AST']/bucks['GP']
pergame.insert(2, 'apg', AST_GP, True)
pergame


# In[17]:


# rpg = rebounds per game
TRB_GP = bucks['TRB']/bucks['GP']
pergame.insert(3, 'rpg', TRB_GP, True)
pergame


# In[18]:


pergame.round({'ppg':2, 'apg':2, 'rpg':2})


# The complete dataframe shows that Giannis led the team in scoring at 29.48 points per game, assists at 5.62 per game, and rebounds at 13.59 per game. There were 6 players that averaged more than 9 points per game. 3 players averaged more than 4 assists per game. Only 1 player averaged more than 10 rebounds per game, with the next closest coming at 6.16.
# 
# After completing the analysis, I came away in awe of the impact of Giannis. As an avid Bucks fan, I readily see what he does on the court and for the organization, but to see it in numbers further defends how much the Bucks rely on him. 
# 
# Some improvements that I thought of at the conclusion of this project include:
# 1. A deeper dive into how stats compare around a division or conference. A bigger analysis would include a league-wide comparison.
# 2. Build ranking and sorting functions into the analysis
# 3. Put parameters on who can be included in the analysis such as, X amount of games would need to be played in order to be included.
# 4. See how the departures and additions of rosters impact the team.
# 
# I hope this analysis was clear and helpful. I would certainly appreciate any comments, tips, or suggestions. This project will be available on my website hoopsdata.com with more to come!
