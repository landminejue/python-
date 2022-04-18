# -*- coding:utf-8 -*-
# author:landmine time:2022/4/6
# 时间复杂度 O(nlogn)
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1: ] if i <= pivot]
        greater = [i for i in array[1: ] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print quicksort([6,1,3,5,8,10])

# 方法二
def quick_sort(array, start, end):

    # 基线条件：递归的退出条件
    if start >= end:
        return

    #设置基准元素：将起始值设置为基准元素
    mid = array[start]
    #low为序列左边的由左向右移动的游标（索引）
    low = start
    #high为序列右边的由右向左的游标（索引）
    high = end

    while low < high:
        while low < high and array[high] >= mid:
            high -= 1
        array[low] = array[high]

        while low < high and array[low] < mid:
            low += 1
        array[high] = array[low]

    array[low] = mid

    quick_sort(array, start, low-1)
    quick_sort(array, low+1, end)

array = [66,7,12,34,45,14,87,11,99]
quick_sort(array, 0, len(array)-1)
print array