class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l, r = 0, 0
        Sum = nums[0]
        Min = len(nums)*2 +100

        while l <= r and r <= len(nums)-1:
            if Sum >= target:
                Min = min(Min, r-l+1)
                Sum -= nums[l]
                l +=1
            # elif Sum >target:
            #     Sum -= nums[l]
            #     l +=1
            else:
                r+=1
                if r < len(nums):
                    Sum += nums[r]

        if Sum == target:
                Min = min(Min, r-l)
                
        return Min if Min != len(nums)*2 +100 else 0

 



