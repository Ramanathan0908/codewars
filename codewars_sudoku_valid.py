from math import sqrt

class Sudoku(object):
    def __init__(self, data):
        self.square = data
    def is_valid(self):
        copy = [x[:] for x in self.square]
        copy2 = [x[:] for x in self.square]
        copy3 = [x[:] for x in self.square]
        N = len(self.square)
        sample = [i for i in range(1, N + 1)]
        little_square = [[] for i in range(0, N)]
        for i, row in enumerate(copy3):
            for j, val in enumerate(row):
                if type(val) is not int:
                    return False
                little_square[(i // int(sqrt(N))) * int(sqrt(N)) + (j // int(sqrt(N)))].append(val)
        for lil in little_square:
            lil.sort()
            if lil != sample:
                return False
        for row in copy:
            row.sort()
            if row != sample:
                return False
        colms = [list(x) for x in zip(*copy2)]
        for col in colms:
            col.sort()
            if col != sample:
                return False

        return True

badSudoku2 = Sudoku([
  [1,2,3,4,5],
  [1,2,3,4],
  [1,2,3,4],  
  ['>']
])

print(badSudoku2.is_valid())

