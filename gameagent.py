# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:57:54 2019

@author: dgill
"""

class GameAgent:
    def __init__(self, game_state):
        self._game_state = game_state
        
    def update_state(self, state):
        self._game_state = state

    def best_move(self):
        return max(
            map(
                lambda move: (move, self._min_play(move)),
                self._game_state.children                  
            ),
            key = lambda tpl: tpl[1]
        )[0]
            
    def _min_play(self, game_state):
        if game_state.is_terminal:
            return game_state.utility
        return min(
            map(
                lambda move: self._max_play(move),
                game_state.children
            )
        )
            
    def _max_play(self, game_state):
        if game_state.is_terminal:
            return game_state.utility
        return max(
            map(
                lambda move: self._min_play(move),
                game_state.children
            )
        )