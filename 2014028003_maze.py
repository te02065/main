n = int(input("row : "))
m = int(input("col : "))
#리스트 선언, 벽 만들기
maze = [[1 for col in range(m+2)] for row in range(n+2)]
mark = [[0 for col in range(m+2)] for row in range(n+2)]
stack = []
print(maze)

class stack:
    def push(self, value):
        if self.isFull():
            raise RuntimeError("StackFullException")
        self.data.append(value)

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("StackFullException")
        return self.data.pop()

    def top(self):
        if self.isEmpty():
            raise RuntimeError("StackFullException")
        return self.data[len(self.data)-1]

    def size(self):
        return len(self.data)

    def printStack(self):
        print(self.data)


class basic:
    row = 1
    col = 1
    dir = 1

#미로 입력
for i in range(1,n+1):
    for j in range(1,m+1):
        maze[i][j] = int(input())
print(maze)

mark[1][1] = 1
top = 0
position = basic()
next = basic()
stack = basic()

exitR = n-1
exitC = m-1
while top >-1 & False:

    row = position.row
    col = position.col
    dir = position.dir
    while dir < 8 & False:
        next.row = row + i
        next.col = col + j
        idx = [-1, -1, 0, 1, 1, 1, 0, -1]
        idy = [0, 1, 1, 1, 0, -1, -1, -1]
        for k in range(len(idx)):
           if next.row == exitR & next.col == exitC:
                True
           elif maze[next.row][next.col] == False & mark[next.row][next.col] == False:
               mark[next.row][next.col] = 1
               position.row = row
               position.col = col
               position.dir = ++dir
               row = next.row
               col = next.col
               dir = 0
           else:
               ++dir

print("the path is: ")
print("row col ")
for i in range(top):
    print("%2d%5d"%(stack[i].row, stack[i].col))
print("%2d%5d"% (row, col))
print("%2d%5d"%(exitR, exitC))




