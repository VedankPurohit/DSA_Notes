class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        Valid = set([i for i in range(len(triplets))])
        print(Valid)
        Can = set()

        for t in range(len(target)):
            num = target[t]
            for i in range(len(triplets)):
                if i not in Valid:
                    continue
                if triplets[i][t] > num:
                    Valid.remove(i)
        print(Valid)
        check = [0,0,0]

        for t in range(len(target)):

            for i in Valid:
                if check[t] == 1:
                    break
                if triplets[i][t] == target[t]:
                    check[t] = 1
        return True if sum(check) == 3 else False