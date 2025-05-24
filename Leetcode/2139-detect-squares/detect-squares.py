class DetectSquares:

    def __init__(self):
        self.Map = {}
        self.col = {}
        self.row = {}
        

    def add(self, point: List[int]) -> None:

        if (point[0],point[1]) not in self.Map:
            self.Map[(point[0],point[1])] = 0
        self.Map[(point[0],point[1])] +=1

        if point[0] not in self.col:
            self.col[point[0]] = []
        self.col[point[0]].append(point[1])

        if point[1] not in self.row:
            self.row[point[1]] = []
        self.row[point[1]].append(point[0])
        

    def count(self, point: List[int]) -> int:
        x =point[0]
        y = point[1]
        if point[0] not in self.col or point[1] not in self.row:
            return 0
        posY = self.col[point[0]] # all points in the point's Y axis
        posX = self.row[point[1]] # all points in the point's X axis

        count = 0

        for i in posX:
            if i == x or (i,y) not in self.Map:
                continue
            for j in posY:
                if j== y or (x,j) not in self.Map or abs(point[0] - i) != abs(point[1]-j):
                    continue
                if (i,j) in self.Map:
                    count += self.Map[(i,j)]
        return count



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)