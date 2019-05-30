#translate cardlist to cardheap
clist = [3,3,3,3,4,4,4,4,6,6,6,8,9,10,11,12,12]
def list_to_heap(c_list):
    c_heap = []
    for i in range(3,18):
        c_heap.append([i,0])
    for card in c_list:
        c_heap[card - 3][1] += 1
    return c_heap

def heap_to_list(c_heap):
    c_list = []
    for cards in c_heap:
        for i in range(cards[1]):
            c_list.append(cards[0])
    return c_list

print(list_to_heap(clist))
print(heap_to_list(list_to_heap(clist)))