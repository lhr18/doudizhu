#from card import *
min_card = 3
max_card = 17

clist = [(3,1),(4,1),(5,1),(6,1),(7,1),(8,0),(9,0),(10,3),(11,4),(12,3),(13,2),(14,1),(15,0),(16,1),(17,1)]
card = {3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Jack', 
        12: 'Queen', 13: 'King', 14: 'A', 15: '2', 16: 'Joker_low', 17: 'Joker_high'}

def getcard(cardlist, n):

    return cardlist[n - min_card]

def divide(cardlist):
    card_dict = {}
    #single
    card_dict['single'] = []
    for i in range(min_card, max_card + 1):
        if getcard(cardlist, i)[1] == 1:
            card_dict['single'].append(i)
    #pair
    card_dict['pair'] = []
    for i in range(min_card, max_card + 1):
        if getcard(cardlist, i)[1] == 2:
            card_dict['pair'].append(i)
    #trible0
    card_dict['trible0'] = []
    for i in range(min_card, max_card + 1):
        if getcard(cardlist, i)[1] == 3:
            card_dict['trible0'].append(i)
    #trible1
    card_dict['trible1'] = []
    #trible2
    card_dict['trible2'] = []

    #straight5
    card_dict['straight5'] = []
    for i in range(min_card, max_card - 6):
        if  getcard(cardlist, i)[1] > 0 and\
            getcard(cardlist, i + 1)[1] > 0 and\
            getcard(cardlist, i + 2)[1] > 0 and\
            getcard(cardlist, i + 3)[1] > 0 and\
            getcard(cardlist, i + 4)[1] > 0:
            card_dict['straight5'].append(i)
    for i in card_dict['straight5']:
        for j in range(i, i + 5):
            if getcard(cardlist, j)[1] == 2:
                card_dict['single'].append(j)
            elif getcard(cardlist, j)[1] == 3:
                card_dict['pair'].append(j)
            elif getcard(cardlist, j)[1] == 4:
                card_dict['trible0'].append(j)
    #straight6
    card_dict['straight6'] = []
    for i in range(len(card_dict['straight5']) - 1):
        if card_dict['straight5'][i + 1] == card_dict['straight5'][i] + 1:
            card_dict['straight6'].append(card_dict['straight5'][i])
    #straight7
    card_dict['straight7'] = []
    for i in range(len(card_dict['straight6']) - 1):
        if card_dict['straight6'][i + 1] == card_dict['straight6'][i] + 1:
            card_dict['straight7'].append(card_dict['straight6'][i])
    #straight8
    card_dict['straight8'] = []
    for i in range(len(card_dict['straight7']) - 1):
        if card_dict['straight7'][i + 1] == card_dict['straight7'][i] + 1:
            card_dict['straight8'].append(card_dict['straight7'][i])
    #straight9
    card_dict['straight9'] = []
    for i in range(len(card_dict['straight8']) - 1):
        if card_dict['straight8'][i + 1] == card_dict['straight8'][i] + 1:
            card_dict['straight9'].append(card_dict['straight8'][i])
    #straight10
    card_dict['straight10'] = []
    for i in range(len(card_dict['straight9']) - 1):
        if card_dict['straight9'][i + 1] == card_dict['straight9'][i] + 1:
            card_dict['straight10'].append(card_dict['straight9'][i])
    #straight11
    card_dict['straight11'] = []
    for i in range(len(card_dict['straight10']) - 1):
        if card_dict['straight10'][i + 1] == card_dict['straight10'][i] + 1:
            card_dict['straight11'].append(card_dict['straight10'][i])
    #straight12
    card_dict['straight12'] = []
    for i in range(len(card_dict['straight11']) - 1):
        if card_dict['straight11'][i + 1] == card_dict['straight11'][i] + 1:
            card_dict['straight12'].append(card_dict['straight11'][i])
    #even3
    card_dict['even3'] = []
    for i in range(min_card, max_card - 4):
        if  getcard(cardlist, i)[1] > 1 and\
            getcard(cardlist, i + 1)[1] > 1 and\
            getcard(cardlist, i + 2)[1] > 1:
            card_dict['even3'].append(i)
    for i in card_dict['even3']:
        for j in range(i, i + 3):
            if getcard(cardlist, j)[1] == 3:
                card_dict['single'].append(j)
            elif getcard(cardlist, j)[1] == 4:
                card_dict['pair'].append(j)
    #even4
    card_dict['even4'] = []
    for i in range(len(card_dict['even3']) - 1):
        if card_dict['even3'][i + 1] == card_dict['even3'][i] + 1:
            card_dict['even4'].append(card_dict['even3'][i])
    #even5
    card_dict['even5'] = []
    for i in range(len(card_dict['even4']) - 1):
        if card_dict['even4'][i + 1] == card_dict['even4'][i] + 1:
            card_dict['even5'].append(card_dict['even4'][i])
    #even6
    card_dict['even6'] = []
    for i in range(len(card_dict['even5']) - 1):
        if card_dict['even5'][i + 1] == card_dict['even5'][i] + 1:
            card_dict['even6'].append(card_dict['even5'][i])
    #even7
    card_dict['even7'] = []
    for i in range(len(card_dict['even6']) - 1):
        if card_dict['even6'][i + 1] == card_dict['even6'][i] + 1:
            card_dict['even7'].append(card_dict['even6'][i])
    #even8
    card_dict['even8'] = []
    for i in range(len(card_dict['even7']) - 1):
        if card_dict['even7'][i + 1] == card_dict['even7'][i] + 1:
            card_dict['even8'].append(card_dict['even7'][i])
    #even9
    card_dict['even9'] = []
    for i in range(len(card_dict['even8']) - 1):
        if card_dict['even8'][i + 1] == card_dict['even8'][i] + 1:
            card_dict['even9'].append(card_dict['even8'][i])
    #even10
    card_dict['even10'] = []
    for i in range(len(card_dict['even9']) - 1):
        if card_dict['even9'][i + 1] == card_dict['even9'][i] + 1:
            card_dict['even10'].append(card_dict['even9'][i])
    #plane2
    card_dict['plane2'] = []
    for i in range(min_card, max_card - 3):
        if  getcard(cardlist, i)[1] > 2 and\
            getcard(cardlist, i + 1)[1] > 2:
            card_dict['plane2'].append(i)
    for i in card_dict['plane2']:
        for j in range(i, i + 2):
            if getcard(cardlist, j)[1] == 4:
                card_dict['single'].append(j)
    #plane3
    card_dict['plane3'] = []
    for i in range(len(card_dict['plane2']) - 1):
        if card_dict['plane2'][i + 1] == card_dict['plane2'][i] + 1:
            card_dict['plane3'].append(card_dict['plane2'][i])
    #plane4
    card_dict['plane4'] = []
    for i in range(len(card_dict['plane3']) - 1):
        if card_dict['plane3'][i + 1] == card_dict['plane3'][i] + 1:
            card_dict['plane4'].append(card_dict['plane3'][i])
    #plane5
    card_dict['plane5'] = []
    for i in range(len(card_dict['plane4']) - 1):
        if card_dict['plane4'][i + 1] == card_dict['plane4'][i] + 1:
            card_dict['plane5'].append(card_dict['plane4'][i])
    #bomb
    card_dict['bomb'] = []
    for i in range(min_card, max_card - 1):
        if getcard(cardlist, i)[1] == 4:
            card_dict['bomb'].append(i)
    if getcard(cardlist, max_card - 1)[1] == 1 and getcard(cardlist, max_card)[1] == 1:
        card_dict['bomb'].append(max_card - 1)
    
    for key in card_dict.keys():
        card_dict[key] = sorted(list(set(card_dict[key])))

    return card_dict


print(divide(clist))