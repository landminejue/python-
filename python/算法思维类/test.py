# -*- coding:utf-8 -*-
# author:landmine time:2022/3/31
# def countdown(i):
#     print i
#     if i < 1:
#         return    #基线条件：函数不在调用自己，避免无限循环
#     else:
#         countdown(i - 1)   #递归条件：函数调用自己
#
# test = countdown(5)
#
# def greet( name ):
#     print "hello," + name + "!"
#     greet2(name)
#     print "getting ready to say bye..."
#     bye()
#
# def greet2( name ):
#     print "how are you, " + name + "?"
# def bye():
#     print "ok,bye!"
#
# test_name = greet("yuhonglei")
#
# num = input("Enter a number: ")
# def recur_factorial(n):
#     if n == 1:
#         return n
#     elif n < 1:
#         return ("NA")
#     else:
#         return n*recur_factorial(n-1)
# print (recur_factorial(int(num)))

# def sum(arr):
#     total = 0
#     for i in arr:
#         total += i
#     return total
# print sum([1,2,3,4])

new_list = []
data = raw_input()[::-1]
if int(data[0]) != 0:
    for i in data:
        if i not in new_list:
            new_list.append(i)
else:
    print("error,not recognized zero")
print(''.join(new_list))
