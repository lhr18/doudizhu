#!/usr/bin/python3

from game import Game

mygame = Game()
for turn in range(2):
    mygame.prepare()
    winner = mygame.start()
    print("winner is " + winner)