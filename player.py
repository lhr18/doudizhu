from divide_best import divide
from divide_best import clean_list
    
class Player:
    """一个简单的玩家"""
    #构造
    def __init__(self, str):
        self.name = str;
        return
    #获取初始手牌
    def get(self, cardlist):
        self.hand = self.list_to_heap(cardlist)
        self.hand_combo = divide(self.hand)
        return
    #一次出牌
    def throw(self, curr_combo, curr_score):       
        #TODO:trible_single is not completed
        if curr_combo == 'null' : #优先出小牌 #TODO:finish the strategy
            for key in self.hand_combo:
                if self.hand_combo[key] :#找到了第一个可以出的牌
                    ret_val = self.hand_combo[key][0]
                    del self.hand_combo[key][0]
                    if self.check_win() :
                        return ['winner', ret_val]
                    return [key, ret_val]
        if self.hand_combo[curr_combo] :
            for i in range(len(self.hand_combo[curr_combo])) :
                if self.hand_combo[curr_combo][i] > curr_score :
                    ret_val = self.hand_combo[curr_combo][i]
                    del self.hand_combo[curr_combo][i]
                    if self.check_win() :
                        return ['winner', ret_val]
                    return [curr_combo, ret_val]
        return ['pass', 0] #不要
        
    def check_win(self):
        for key in self.hand_combo:
            if self.hand_combo[key] :
                return False
        return True#I'm winner 
    
    #整理拿到的17张牌
    def list_to_heap(self,c_list):
        c_heap = []
        for i in range(3,18):
            c_heap.append([i,0])
        for card in c_list:
            c_heap[card - 3][1] += 1
        return c_heap
    
    def heap_to_list(self,c_heap):
        c_list = []
        for cards in c_heap:
            for i in range(cards[1]):
                c_list.append(cards[0])
        return c_list

class YZQ:
    """一个简单的玩家"""
    #构造
    def __init__(self, str):
        self.name = str;
        return
    #获取初始手牌
    def get(self, cardlist):
        self.hand = self.list_to_heap(cardlist)
        #self.hand_combo = divide(self.hand)
        return
    #一次出牌
    def throw(self, curr_combo, curr_score):
        print("LJR剩余手牌:")
        print(clean_list(self.hand))
        inputcombo = input("输入牌型")
        if inputcombo == 'pass' :
            return ['pass',0]
        inputscore = int(input("score"))
        x=input("出牌列表")
        xlist=x.split(",")
        xlist = [int(xlist[i]) for i in range(len(xlist))]
        for cardd in xlist:
            self.hand[cardd-3][1] -= 1
        return [inputcombo, inputscore]
    
    #整理拿到的17张牌
    def list_to_heap(self,c_list):
        c_heap = []
        for i in range(3,18):
            c_heap.append([i,0])
        for card in c_list:
            c_heap[card - 3][1] += 1
        return c_heap
    
    def heap_to_list(self,c_heap):
        c_list = []
        for cards in c_heap:
            for i in range(cards[1]):
                c_list.append(cards[0])
        return c_list