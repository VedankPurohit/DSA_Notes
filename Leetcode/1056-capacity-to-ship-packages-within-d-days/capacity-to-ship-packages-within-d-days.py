class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Max = (max(weights)*len(weights))//days
        Max = max(weights)*len(weights)
        Min = max(sum(weights)//days, max(weights))

        print(Min, Max)

        def checker(cap):
            curSum = 0
            N = 1
            i = 0 
            while i< len(weights):
                if weights[i] > cap:
                    return False
                curSum += weights[i]
                if curSum > cap:
                    N +=1
                    curSum = 0
                else:
                    i+=1
            return N <= days
        
        # print(checker(5))

        for i in range(Min, Max+1):
            # print("Hii")
            if checker(i):
                return i
        

        # return Max
                
