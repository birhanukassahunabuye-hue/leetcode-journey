class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        for num in nums:
            digits = 0
            while num:
                digits +=1
                num //=10
            if digits % 2 ==0:
                cnt+=1
        return cnt
        
        