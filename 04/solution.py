with open('input.txt') as f:
    data = f.read()

class Board:
    def __init__(self):
        self.grid = [[0 for _ in range(5)] for _ in range(5)]
        self.marked = [[False for _ in range(5)] for _ in range(5)]
        self.is_complete = False

    @classmethod
    def parse_from_string(self, s):
        ret = Board()
        for i, row in enumerate(s.split('\n')):
            ret.grid[i] = [int(x) for x in row.split()]
        return ret
    
    def mark(self, nbr):
        for i in range(5):
            for j in range(5):
                if self.grid[i][j] == nbr:
                    self.marked[i][j] = True
    
    def check(self):
        if any(all(row) for row in self.marked):
            return True
        if any(all(col) for col in zip(*self.marked)):
            return True
        return False
    
    def count(self):
        count = 0
        for i in range(5):
            for j in range(5):
                if self.marked[i][j] == False:
                    count += self.grid[i][j]
        return count

groups = data.split('\n\n')
nums = [int (x) for x in groups[0].split(',')]
boards = [Board.parse_from_string(s) for s in groups[1:]]


results = []
for num in nums:
    for board in boards:
        if board.is_complete:
            continue
        board.mark(num)
        if board.check():
            board.is_complete = True
            results.append(board.count() * num)
print("Part 1:", results[0]) # 10680
print("Part 2:", results[-1]) # 31892
