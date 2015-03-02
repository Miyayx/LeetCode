# -*- coding:utf-8 -*-
class Solution:
    # @param num, a list of integer
    # @return an integer

    def longestConsecutive(self, num):
        m = 0 #当前最长
        l = num
        for n in num:
            if n in l:#还没有被找到过，可以继续进行连续数列的查找
                mm = 1 #记录本次连续数列的长度
                a = n
                while a-1 in l:
                    l.remove(a-1) #被分析过了就删除
                    mm += 1
                    a = a-1
                a = n
                while a+1 in l:
                    l.remove(a+1)
                    mm += 1
                    a = a+1
                if m < mm:
                    m = mm
        return m

#Accepted
