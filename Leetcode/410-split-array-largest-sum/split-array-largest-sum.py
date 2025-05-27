class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        Min = max(sum(nums)//k, max(nums))
        Max = sum(nums)

        def checker(cap):
            curSum = 0
            N = 1
            i = 0 
            while i< len(nums):
                if nums[i] > cap or N >k:
                    return False
                curSum += nums[i]
                if curSum > cap:
                    N +=1
                    curSum = 0
                else:
                    i+=1
            return N <= k

        l = Min
        r = Max +1
        # print(l,r)
        out =r
        while r >=l:
            print(l,r)
            mid = (r+l)//2
            if checker(mid):
                out = min(out,mid)
                r = mid-1
            else:
                l = mid+1
        return out
        
