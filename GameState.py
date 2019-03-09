# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:00:28 2019

@author: dgill
"""

from copy import deepcopy
from decutils import timer

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
        
        tester = BitWinTester(self._state)
        self._winner = tester.winner()
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
    
class BitWinTester:
    _wins = set([
        0b111000000,
        0b000111000,
        0b000000111,
        0b100100100,
        0b010010010,
        0b001001001,
        0b100010001,
        0b001010100        
    ])
    
    def __init__(self, state):
        self._state = state
        self._o_encoding = self._encoded_state(O)
        self._x_encoding = self._encoded_state(X)
    
    def winner(self):
        if self._x_encoding in BitWinTester._wins:
            return X
        if self._o_encoding in BitWinTester._wins:
            return O
        if self._is_draw():
            return DRAW
        return NEUTRAL
        
    def _is_draw(self):
        for tile in self._state:
            if tile == BLANK_FLAG:
                return False
        return True

    def _encoded_state(self, player):
        accum = 0
        for i in range(9):
            if self._state[i] == player:
                accum += (2 ** i)
        return accum
    
state = [X, X, X, 0, O, 0, 0, 0, O]
gs = GameState(O, state)
print(gs.is_terminal())
print(gs._winner)