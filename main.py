#!/usr/bin/python3

from game import Game

def list_to_heap(c_list):
    c_heap = []
    for i in range(3,18):
        c_heap.append([i,0])
    for card in c_list:
        c_heap[card - 3][1] += 1
    return c_heap
'''
mygame = Game()
#for turn in range(1):

mygame.prepare()
winner = mygame.start()
print("winner is " + winner)
'''
for test_turn in range(10):
    yzq_win=0
    ljr_win=0
    lhr_win=0
    fo = open("foo.txt","w")
    for i in range(600):
        mygame = Game()
        handlist = mygame.prepare()#默认yzq是地主
        
        #特征提取
        single_len = []
        for pid in range(3):
            single_len.append(len(mygame.plist[pid].hand_combo['single']))
        pair_len = []
        for pid in range(3):
            pair_len.append(len(mygame.plist[pid].hand_combo['pair']))
        
        winner = mygame.start()
        if winner == 'yzq':
            yzq_win += 1
        elif winner == 'ljr':
            ljr_win += 1
            lhr_win += 1
        elif winner == 'lhr':
            lhr_win += 1
            ljr_win += 1
        #win_code
        if winner == 'yzq':
            win_code = [1,0,0]
        elif winner == 'ljr':
            win_code = [0,1,1]
        elif winner == 'lhr':
            win_code = [0,1,1]
        #role_code
        role_code = [1,0,0]
        #
        for pid in range(3):
            #for cardname in range(15):
                #fo.write(str(list_to_heap(handlist[pid][0:17])[cardname][1])+" ")
            fo.write(str(pair_len[pid])+" "+str(single_len[pid])+" "+str(role_code[pid])+" "+str(win_code[pid])+" "+"\n")
        #print(list_to_heap(handlist[0][0:17]))
    fo.close()


    import numpy as np
    raw_data = np.loadtxt("foo.txt")
    test_size = int(len(raw_data)/5)
    feature_size = len(raw_data[0])-1
    test = raw_data[:test_size]
    train = raw_data[test_size:]
    train_feature = train[...,0:feature_size]
    train_lable = train[...,feature_size]
    test_feature = test[...,0:feature_size]
    test_lable = test[...,feature_size]

    from sklearn.svm import SVC
    clf = SVC(gamma='auto')
    clf.fit(train_feature, train_lable)
    SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
        decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
        max_iter=-1, probability=False, random_state=None, shrinking=True,
        tol=0.001, verbose=False)
    pre_res = clf.predict(test_feature)
    count_win = 0
    for i in range(len(test)):
        if pre_res[i] == test_lable[i]:
            count_win = count_win +1
    print(count_win/len(test))