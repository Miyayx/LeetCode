class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        s_num = sorted(num)
        for i in range(len(num)):
            a = s_num[i] 
            for j in range(i,len(num)):
                b = s_num[j]
                if b + a > target:
                    break
                if b + a == target:
                    ai = num.index(a)+1
                    bi = num.index(b)+1
                    if ai == bi:
                        bi = num.index(b, ai)+1
                    return sorted([ai, bi])
        return [0,0]

