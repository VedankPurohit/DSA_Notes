class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        zero = ord("0")
        nine = ord("9")
        # ch = chr(zero)
        # print(ch)
        def num(n):
            N = 0
            pos = 1
            for i in range(len(n)-1,-1,-1):
                rep = ord(n[i]) 
                if rep >= zero or rep <= nine:
                    N += (rep - zero)*pos
                    pos *= 10
            if "-" in n:
                return N*-1
            return N
        return str(num(num1) * num(num2))
