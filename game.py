#!/usr/bin/python3
 
from player import Player

class Game:
    def __init__(self):
        # 三个玩家
        p1 = Player("ljr")
        p2 = Player("yzq")
        p3 = Player("lhr")
        self.plist = [p1,p2,p3]
        self.handlist = []
    def prepare(self):
        #发牌
        self.handlist = [[1,2,3,4],[5,6],[1,3,5,7]]
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
                
