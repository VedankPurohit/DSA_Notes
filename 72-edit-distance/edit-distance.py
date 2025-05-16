class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dfs(i,j):
            if j == len(word2):
                return len(word1)-i
            if i == len(word1):
                return (len(word2)-j)   #float("inf")

            if i < 0 or j<0 or i > len(word1) or j > len(word2):
                return float("inf")
            
            if (i,j) in cache:
                return cache[(i,j)]

            normal = float("inf")
            if word1[i] == word2[j]:
                normal = dfs(i+1,j+1)
            replace = dfs(i+1,j+1) +1

            delete = dfs(i+1,j) +1

            insert = dfs(i,j+1) +1

            cache[(i,j)] = min(normal,replace,delete,insert)


            return cache[(i,j)]
            
        return dfs(0,0)

            

