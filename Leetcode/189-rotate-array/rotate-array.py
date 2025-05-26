class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k %len(nums)
        l , r = 0, len(nums)-1

        def rev(l,r):
            while r> l:
                nums[l] , nums[r] = nums[r], nums[l]
                l +=1
                r -= 1
        rev(l,r)
        rev(0,k-1)
        rev(k,r)
        # print(nums)