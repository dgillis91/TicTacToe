# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:00:28 2019

@author: dgill
"""

class GameState:
    PlayerMin = 0
    PlayerMax = 1
    __blank_flag = 0
    __player_to_sprite_map = ["O", "X"]
    def __init__(self, player, state):
        self._state = state
        self._player = player
        self._actions = None
        self._child_states = None
        
        
    
    
    def __repr__(self):
        str_rep = ''
        for i in range(3):
            for j in range(3):
                str_rep = str_rep + self._state[i + j]