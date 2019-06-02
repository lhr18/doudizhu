#lhr的想法：第一优先级：飞机、炸弹；第二优先级：连对、顺子；第三优先级：三带一、对子、单张
#机器学习设想：根据初始手牌，预测本局胜负；用历史作战记录进行训练

#from card import *
from operator import eq
min_card = 3
max_card = 17
'''
clist = [[3,1],[4,1],[5,3],[6,2],[7,2],[8,0],[9,3],[10,1],[11,1],[12,3],[13,3],[14,3],[15,1],[16,1],[17,1]]
card = {3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Jack', 
        12: 'Queen', 13: 'King', 14: 'A', 15: '2', 16: 'Joker_low', 17: 'Joker_high'}
'''
#获取名为cardname的牌的剩余数量
def getcard(cardlist, cardname):
    return cardlist[cardname - min_card]

#从cardlist中，将cardname的牌减少num张
def delcard(cardlist, cardname, num):
    cardlist[cardname - min_card][1] -= num;
    return

#从cardlist中，删除planestart开始的num飞机
def delcard_plane(cardlist, planestart, num):
    for i in range(num):
        delcard(cardlist, planestart + i, 3)
    return

#从cardlist中，删除evenstart开始的num连对
def delcard_even(cardlist, evenstart, num):
    for i in range(num):
        delcard(cardlist, evenstart + i, 2)
    return

#从cardlist中，删除straightstart开始的num顺子
def delcard_straight(cardlist, straightstart, num):
    for i in range(num):
        delcard(cardlist, straightstart + i, 1)
    return

def divide(cardlist):
    card_dict = {}
    #bomb
    card_dict['bomb'] = []
    for i in range(min_card, max_card - 1):
        if getcard(cardlist, i)[1] == 4:
            card_dict['bomb'].append(i)
            delcard(cardlist, i, 4)
    #王炸
    if getcard(cardlist, max_card - 1)[1] == 1 and getcard(cardlist, max_card)[1] == 1:
        card_dict['bomb'].append(max_card - 1)
        delcard(cardlist, max_card - 1, 1)
        delcard(cardlist, max_card, 1)
    #plane
    for i in range(2,6):
        card_dict['plane'+str(i)] = []
    rank_plane = 0 #飞机的级别
    for i in range(min_card, max_card-1): #飞机最高连到A        
        if  getcard(cardlist, i)[1] >= 3 and i < max_card-2:
            rank_plane += 1
            continue
        else:
            if rank_plane >= 2:
                card_dict['plane'+str(rank_plane)].append(i-rank_plane)
                delcard_plane(cardlist, i-rank_plane, rank_plane)
                #重新计数
            rank_plane = 0
    #顺子和连对复杂一点，不过先用最简单的策略：优先顺子
    #TODO:how to devide straight and even?
    #even
    for i in range(3,11):
        card_dict['even'+str(i)] = []
    rank_even = 0 #连对的级别
    for i in range(min_card, max_card-1): #连对最高连到A        
        if  getcard(cardlist, i)[1] >= 2 and i < max_card-2:
            rank_even += 1
            continue
        else:
            if rank_even >= 3:
                card_dict['even'+str(rank_even)].append(i-rank_even)
                delcard_even(cardlist, i-rank_even, rank_even)
                #重新计数
            rank_even = 0
    #straight
    for i in range(5,13):
        card_dict['straight'+str(i)] = []
    rank_straight = 0 #顺子的级别
    for i in range(min_card, max_card-1): #顺子最高连到A        
        if  getcard(cardlist, i)[1] >= 1 and i < max_card-2:
            rank_straight += 1
            continue
        else:
            if rank_straight >= 5:
                card_dict['straight'+str(rank_straight)].append(i-rank_straight)
                delcard_straight(cardlist, i-rank_straight, rank_straight)
                #重新计数
            rank_straight = 0
    #trible
    card_dict['trible0'] = []
    for i in range(min_card, max_card - 1): #检查到2        
        if getcard(cardlist, i)[1] == 3:
            card_dict['trible0'].append(i)
            delcard(cardlist, i, 3)
    #pair
    card_dict['pair'] = []
    for i in range(min_card, max_card - 1): #检查到2  
        if getcard(cardlist, i)[1] == 2:
            card_dict['pair'].append(i)
            delcard(cardlist, i, 2)
    #single
    card_dict['single'] = []
    for i in range(min_card, max_card + 1): #检查到2  
        if getcard(cardlist, i)[1] == 1:
            card_dict['single'].append(i)
            delcard(cardlist, i, 1)
    #最后一步，还要给飞机三带一配单张，先考虑有足够的单张
    #TODO:if there is not enough single to fit plane? devide pair into single?
    #plane_single
    card_dict['plane_single'] = []
    plane_single_count = 0;
    for i in range(2,6):
        plane_single_count += i * len(card_dict['plane'+str(i)]);
    for i in range(plane_single_count) :
        #card_dict['plane_single'].append(card_dict['single'][0])#TODO:hide trible_single
        if card_dict['single']:
            del card_dict['single'][0]#TODO:fit plane
    #配三带一，先不考虑三带一对
    card_dict['trible_single'] = []
    card_dict['trible1'] = []
    while card_dict['single'] and card_dict['trible0'] :
        #card_dict['trible_single'].append(card_dict['single'][0])#TODO:hide trible_single
        del card_dict['single'][0]
        card_dict['trible1'].append(card_dict['trible0'][-1])
        del card_dict['trible0'][-1]
        
    
    return card_dict



#去除0项，使打印更清爽
def clean_list(oldlist):
    newlist = []
    for card in oldlist:
        if card[1] > 0:
            newlist.append(card)
    return newlist

#去除空项，使打印更清爽
def clean_dict(olddict):
    newdict = {}
    for key in olddict:
        if not eq(olddict[key], []):
            newdict[key] = olddict[key]
    return newdict
'''
print(clean_list(clist))
dic = divide(clist)
#print(dic)
print(clean_dict(dic))
#print(clist)    
if clean_list(clist):
    print("divide error")
'''

