class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
         prefix_sum = {0: 1}
         curr_sum = 0
         count = 0
         for num in nums:
              curr_sum +=num
              needed = curr_sum -k

              if needed in prefix_sum:
                     count += prefix_sum[needed]


              prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

         return count

               
        
