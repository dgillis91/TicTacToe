# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 12:37:35 2019

@author: dgill
"""

from GameState import GameState
from GameState import X, O
from gameagent import GameAgent
from observable import Observable
from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

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
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()
#    runner = GameRunner()
#    runner.play()
    