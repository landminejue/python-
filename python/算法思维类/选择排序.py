# -*- coding:utf-8 -*-
# author:landmine time:2022/3/31
# 时间复杂度 O(n^2)
def findSmalllest(arr):
    # 找出数组中最小元素
    smalllest = arr[0]  #存储最小的值
    smalllest_index = 0  #存储最小元素的索引
    for i in range(1, len(arr)):
        if arr[i] < smalllest:
            smalllest = arr[i]
            smalllest_index = i
    return smalllest_index

def selectionSort(arr):
    newarr = []
    for i in range(len(arr)):
        smalllest = findSmalllest(arr)
        # append:在列表末尾添加新的对象    pop:移除列表中的元素（默认为最后一个元素），并返回改元素的值
        newarr.append(arr.pop(smalllest))
    return newarr

print selectionSort([5,7,2,3,9,1,4])
