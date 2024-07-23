#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 16:45:54 2021

@author: deniz
"""
import numpy as np

class tictactoe():
    def __init__(self):
        self.tics= np.zeros((3,3))
        self.tacs= np.zeros((3,3))
    
    def reset(self):
        self.tics= np.zeros((3,3))
        self.tacs= np.zeros((3,3))
        self.render()
        
    def tic(self,ticpos):
        self.validate_move(ticpos)
        self.tics[ticpos] = True
        self.render()
        self.checkwin()
        
    def tac(self,tacpos):
        self.validate_move(tacpos)
        self.tacs[tacpos] = True
        self.render()
        self.checkwin()

    def render(self):
        self.string=''      
        
        cnt=0
        for x in [(x,y) for x in range(3) for y in range(3)]:
            if self.tics[x]!=0:
                self.string += " x "
            elif self.tacs[x]!=0:
                self.string += " o "
            else:
                self.string += " _ "
            if cnt%3==2:
                print(self.string)
                print('\n')
                self.string = ''
            cnt+=1

    def validate_move(self,newpos):
        if newpos not in [(x,y) for x in range(3) for y in range(3)]:
            raise ValueError("Stay inside the board")
        elif self.tics[newpos]==True:
            raise Exception("Wrong move,there is a tic there, play again!")
        elif self.tacs[newpos]==True:
            raise Exception("Wrong move,there is a tac there, play again!")
    
    def checkwin(self):
        if self.tics.trace()==3 or np.fliplr(self.tics).trace()==3:
            print("Tic wins")
            self.reset()
            return 0
        if self.tacs.trace()==3 or np.fliplr(self.tacs).trace()==3:
            print("Tac wins")
            self.reset()
            return 1

        else:
            for x in range(3):
                if sum(self.tics[x])==3 or sum(self.tics[:,x])==3:
                    print("Tic wins")
                    self.reset()
                    return 0

                elif sum(self.tacs[x])==3 or sum(self.tacs[:,x])==3:
                    print("Tac wins")
                    self.reset()
                    return 1
       
#%%         
game = tictactoe()        
game.reset()
game.render()
game.tic((2,2))
game.tac((1,0))

game.tic((0,0))
game.tac((1,1))
game.tic((2,1))
game.tac((1,2))
# Tac wins

    
    
