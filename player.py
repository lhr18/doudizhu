from divide_best import divide

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
        flag = 0
        for key in self.hand_combo:
            if self.hand_combo[key] :
                flag = 1
        if flag == 0 :
            return ['winner', 0]#I'm winner
        #TODO:trible_single is not completed
        if curr_combo == 'null' : #优先出小牌 #TODO:finish the strategy
            for key in self.hand_combo:
                if self.hand_combo[key] :#找到了第一个可以出的牌
                    ret_val = self.hand_combo[key][0]
                    del self.hand_combo[key][0]
                    return [key, ret_val]
        if self.hand_combo[curr_combo] :
            for i in range(len(self.hand_combo[curr_combo])) :
                if self.hand_combo[curr_combo][i] > curr_score :
                    #TODO:print I win
                    ret_val = self.hand_combo[curr_combo][i]
                    del self.hand_combo[curr_combo][i]
                    return [curr_combo, ret_val]
        return ['pass', 0] #不要
        
    
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

