class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    
        for i in range(len(nums)-2,-1,-1):
            prev = nums[i+1]
            now = nums[i] + prev
            nums[i] = max(nums[i],now)
        return max(nums)







        # Max = nums[0]
        # curMax = 0
        # for n in nums:
        #     print(n)
        #     curMax = max(curMax, 0) + n
        #     print(f" cur Max - {curMax}")
        #     Max = max(Max, curMax)
        #     print(f"Max - {Max}")
        # return Max
