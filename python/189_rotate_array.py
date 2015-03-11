class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.

    def rotate(self, nums, k):
        #Method 1
        for i in range(k):
            nums.insert(0, nums.pop())




