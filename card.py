
#不同大小的牌
card = {3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'A', 15: '2', 16: 'Joker_low', 17: 'Joker_high'}
#牌型：空、单张、对子、三个不带、三带一、三带一对、顺子5~12、连对3~10、飞机2~5、炸弹
combo = {'null': 0, 'single': 1, 'pair': 2, 'trible0': 3,  'trible1': 4, 'trible12': 5, 'straight5': 6, 'straight6': 7, 'straight7': 8, 'straight8': 9, 'straight9': 10, 'straight10': 11, 'straight11': 12, 'straight12': 13, 'even3': 14, 'even4': 15, 'even5': 16, 'even6': 17, 'even7': 18, 'even8': 19, 'even9': 20, 'even10': 21, 'plane2': 22, 'plane3': 23, 'plane4': 24, 'plane5': 25, 'bomb': 26}
'''
class CardHeap:
    #heap的结构：[[牌,数量],,,,]
    #用牌列表来转换生成吗？感觉没想好怎么用
    def __init__(self,cardlist):
        #TODO:translate cardlist into heap
'''
class CardComment:
    #comment的结构：[牌型，分数]
    def __init__(self,str,score):
        self.combo = str
        self.score = score
'''        
class CardCombo:
    #出牌接口用这个数据结构吗？
    #CardCombo的结构[CardHeap, CardComment]
    def __init__(self,CardHeap,CardComment):
        #TODO:combo
'''
