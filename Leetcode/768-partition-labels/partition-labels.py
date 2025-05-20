class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        HashMap = {}
        Lis = []

        for i in range(len(s)):
            HashMap[s[i]] = i
        Max = HashMap[s[0]]
        for a in range(len(s)):
            Max = max(Max, HashMap[s[a]])
            if a == Max:
                Max += 1
                Lis.append(a+1)
        Lis = Lis[::-1]
        for a in range(len(Lis)-1):
            Lis[a] = Lis[a] - Lis[a+1]
        Lis = Lis[::-1]
        
        return Lis


        