#!/usr/bin/python3
 
from player import Player
from player import YZQ
from random import shuffle

class Game:
    def __init__(self):
        # 三个玩家
        p1 = Player("yzq")
        p2 = Player("ljr")
        p3 = Player("lhr")
        self.plist = [p1,p2,p3]
        #本轮出牌
        self.curr_player = 0 #TODO: note
        self.curr_combo = "null"
        self.curr_score = 0
    def prepare(self):
        #发牌
        all_cards = list(range(3,16)) * 4 + [16,17]
        shuffle(all_cards)
        self.handlist = [all_cards[0:20],all_cards[20:37],all_cards[37:54]]
        for pid in range(3):    
            self.plist[pid].get(self.handlist[pid])
        '''
        #展示初始手牌
        for pid in range(3):    
            print(self.plist[pid].name+":")
            print(sorted(self.handlist[pid]))
            '''
        return self.handlist
    def start(self):
        #TODO:check illegal
        while 1:
            for pid in range(3):
                if self.curr_player != pid:
                    throw_card = self.plist[pid].throw(self.curr_combo, self.curr_score)
                else:
                    throw_card = self.plist[pid].throw('null', self.curr_score)
                #TODO:check the winner
                if throw_card[0] == 'winner':
                    #print(self.plist[pid].name+":"+self.curr_combo+":"+str(throw_card[1]))
                    return self.plist[pid].name
                if throw_card[0] == 'pass':
                    #print(self.plist[pid].name+":"+"不要")
                    'aa'
                else:
                    self.curr_player = pid
                    self.curr_combo = throw_card[0]
                    self.curr_score = throw_card[1]
                    #print(self.plist[pid].name+":"+throw_card[0]+":"+str(throw_card[1]))
                
        