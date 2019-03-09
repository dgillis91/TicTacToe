# Tic Tac Toe

## Introduction
This is a simple implementation of an AI which cannot lose at tic tac toe. 
The AI is implemented using the minimax algorithm. While faster algorithms
such as alpha-beta pruning exist, the number of possible states in a game
is small enough for decent performance with minimax.

## Rules
Tic tac toe is a two-player board game consisting of a three by three board.
The first player to get three pieces in a row wins. If a state arises in which 
no player can get three in a row, the game is a tie, also referred to as a 
cat game.  

The players are represented by the pieces they are playing, either
"X" or "O". In the standard game, "X" always goes first. 