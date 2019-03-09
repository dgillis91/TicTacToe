# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:00:28 2019

@author: dgill
"""

from copy import deepcopy

DRAW = 'D'
NEUTRAL = 'N'
O = 'O'
X = 'X'

PLAYERS = [O, X]
BLANK_FLAG = 0

class GameState:
    PlayerMin = 0
    PlayerMax = 1
    def __init__(self, player, state):
        self._state = state
        self._player = player
    
        self._actions = None
        
        self._winner = WinTester(self._state).winner()
        self._utility = self._utility_function(self._winner)
        
    @property
    def utility(self):
        return self._utility
    
    # Don't have children as a property - no reason to evaluate if this is
    # a terminal state.
    def children(self):
        states = []
        move_indices = [
            i for i, x in enumerate(self._state)
            if x == self._player
        ]
        for move_index in move_indices:
            board = deepcopy(self._state)
            board[move_index] = self._player
            states.append(board)
        return states
    
    def is_terminal(self):
        return self._winner != NEUTRAL
    
    def _utility_function(self, winner):
        utility = 0
        if winner == X:
            utility = 1
        elif winner == O:
            utility = -1
        return utility
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return '|{}|{}|{}|\n|{}|{}|{}|\n|{}|{}|{}|\n'.format(*list(map(
            lambda x: ' ' if x == 0 else x,
            self._state
        )))
    
class WinTester:
    def __init__(self, state):
        self._state = state
    
    def winner(self):
        for player in PLAYERS:
            for i in range(3):
                row_win = self._is_row_win(i, player)
                col_win = self._is_column_win(i, player)
                if row_win or col_win:
                    return player
            if self._is_diagonal_win(player):
                return player
            
        # Works because we've exhausted wins
        if self._is_draw():
            return DRAW
        
        return NEUTRAL
    
    def _is_row_win(self, row, player):
        row_start_index = 3 * row
        row_stop_index = row_start_index + 3
        for i in range(row_start_index, row_stop_index):
            if self._state[i] != player:
                return False
        return True

    def _is_column_win(self, column, player):
        stop_index = column + 7
        for i in range(column, stop_index, 3):
            if self._state[i] != player:
                return False
        return True
    
    def _is_diagonal_win(self, player):
        diag_one_win = True
        diag_two_win = True
        for i in range(0, 9, 4):
            if self._state[i] != player:
                diag_one_win = False
        for i in range(2, 7, 2):
            if self._state[i] != player:
                diag_two_win = False
        return diag_one_win or diag_two_win
    
    def _is_draw(self):
        for tile in self._state:
            if tile == BLANK_FLAG:
                return False
        return True
    