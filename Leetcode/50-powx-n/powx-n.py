class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1:
            return x 

        def ret(x,num):
            if num == 0:
                return 1
            if num == 1:
                return x
            out = ret(x,num//2)
            out *= out 
            if num %2:
                out *= x
            return out
        out = ret(x,n) if n>=0 else 1/ret(x,-n)
        return out