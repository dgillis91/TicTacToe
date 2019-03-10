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
    def __init__(self, player, state):
        self._state = state
        self._player = player
    
        self._children = self._generate_children()
        
        tester = BitWinTester(self._state)
        self._winner = tester.winner()
        self._utility = self._utility_function(self._winner)
        
    @property
    def utility(self):
        return self._utility
    
    @property
    def children(self):
        for child in self._children:
            yield child

    @property
    def is_terminal(self):
        return self._winner != NEUTRAL
    
    @property
    def player(self):
        return self._player
    
    @property
    def winner(self):
        return self._winner
    
    def move(self, index):
        next_player = self._next_player()
        new_state = self._new_state(self._state, index)
        return GameState(next_player, new_state)
    
    def _generate_children(self):
        states = []
        next_player = self._next_player()
        move_indices = [
            i for i, x in enumerate(self._state)
            if x == BLANK_FLAG
        ]
        self._moves = set(move_indices)
        for move_index in move_indices:
            board = self._new_state(self._state, move_index)
            states.append(GameState(next_player, board))
        return states
    
    def _next_player(self):
        if self._player == O:
            return X
        else:
            return O
    
    def _new_state(self, state, index):
        board = deepcopy(state)
        board[index] = self._player
        return board
    
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
    _wins = [
        0b111000000,
        0b000111000,
        0b000000111,
        0b100100100,
        0b010010010,
        0b001001001,
        0b100010001,
        0b001010100        
    ]
    
    _win_check = set(_wins)
    
    def __init__(self, state):
        self._state = state
        self._o_encoding = self._encoded_state(O)
        self._x_encoding = self._encoded_state(X)
    
    def winner(self):
        for win in BitWinTester._wins:
            x = win & self._x_encoding
            if x in BitWinTester._win_check:
                return X
        for win in BitWinTester._wins:
            o = win & self._o_encoding
            if o in BitWinTester._win_check:
                return O
        if self._is_draw():
            return DRAW
        return NEUTRAL
        
    def _is_draw(self):
        for tile in self._state:
            if tile == BLANK_FLAG:
                return False
        return True

    # Endianess doesn't matter - the game state forms a symmetric 
    # permutation group. This can likely be done faster with a shift.
    def _encoded_state(self, player):
        accum = 0
        for i in range(9):
            if self._state[i] == player:
                accum += (2 ** i)
        return accum
    
if __name__ == '__main__':
    state = [X, X, X, 0, O, 0, 0, 0, O]
    gs = GameState(O, state)
    print(gs.is_terminal())
    print(gs._winner)
    for c in gs.children:
        print(c)