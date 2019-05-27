class Player:
    """一个简单的玩家"""
    #构造
    def __init__(self, str):
        self.name = str;
        return
    #获取初始手牌
    def get(self, handlist):
        self.hand = handlist
        return
    #一次出牌
    def throw(self):
        if len(self.hand)>0:
            ret = self.hand[0]
            #del self.hand[0]
            return ret
        else :
            return -1