class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        out = [intervals[0]]
        for a in intervals:
            # print(out)
            if out[-1][0] <= a[0] and out[-1][1] >= a[0]:
                # print("ii")
                # print([min(out[-1][0],a[0]),max([out[-1][1],a[1]])])
                out[-1] = [min(out[-1][0],a[0]),max([out[-1][1],a[1]])]
            else:
                out.append(a)
        return out
