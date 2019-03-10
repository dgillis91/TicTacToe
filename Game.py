# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 12:37:35 2019

@author: dgill
"""

from GameState import GameState
from GameState import X, O
from observable import Observable

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

class GameRunner(Observable):
    def __init__(self):
        self._initial_state = GameState(X, [0] * 9)
        self._state = self._initial_state
        self._agent = GameAgent(self._initial_state)

    def get_move(self):
        print(self._agent.best_move())
        
    def play(self):
        print('[+] (PROBABLY) UNBEATABLE TIC TAC TOE BOT')
        print('[+] WHEN ASKED TO ENTER A MOVE, USE THE INDICES, BELOW')
        print(GameState(X, list(range(9))))
        while not self._state.is_terminal:
            self._show_board()
            self._next_play()
        print('[+] WINNER: {}'.format(self._state.winner))
        print(self._state)
    
    def _show_board(self):
        print('[+] CURRENT STATE')
        print(self._state)
    
    def _next_play(self):
        if self._state.player == X:
            self._state = self._agent.best_move()
            self._agent.update_state(self._state)
        else:
            play_index = int(input('[+] Enter the index to play: '))
            self._state = self._state.move(play_index)
            self._agent.update_state(self._state)
            
    
if __name__ == '__main__':
    runner = GameRunner()
    runner.play()
    
    