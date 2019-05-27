#!/usr/bin/python3
 
from player import Player
from random import shuffle

class Game:
    def __init__(self):
        # 三个玩家
        p1 = Player("ljr")
        p2 = Player("yzq")
        p3 = Player("lhr")
        self.plist = [p1,p2,p3]
    def prepare(self):
        #发牌
        all_cards = list(range(3,16)) * 4 + [16,17]
        shuffle(all_cards)
        self.handlist = [all_cards[0:20],all_cards[20:37],all_cards[37:54]]
        for pid in range(3):    
            self.plist[pid].get(self.handlist[pid])
    def start(self):
        while 1:
            for pid in range(3):
                throw_card = self.plist[pid].throw()
                if throw_card != -1:
                    #TODO:if you have this card
                    #打出一手牌
                    print(self.plist[pid].name+":"+str(throw_card))
                    self.handlist[pid].remove(throw_card)
                    #判定游戏是否结束
                    if(len(self.handlist[pid])==0):
                        return self.plist[pid].name
                else:
                    print("不要")
                
