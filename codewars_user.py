class User():
    def __init__(self, rank=-8):
        self.rank = rank
        self.progress = 0


    def inc_progress(self, rank):
        if rank < -8 or rank > 8 or rank == 0:
            raise "invalid"
        if (self.rank == rank):
            self.progress_incr(3)
        elif (self.rank - rank == 1):
            self.progress_incr(1)
        elif (self.rank == 1 and rank == -1):
            self.progress_incr(1)
        elif (self.rank < 0 and rank > 0):
            self.progress_incr(10 * (rank - self.rank - 1) * (rank - self.rank - 1))
        elif (self.rank < rank):
            self.progress_incr(10 * (rank - self.rank) * (rank - self.rank))

    def progress_incr(self, progress):
        self.progress += progress
        if self.progress >= 100:
            old_rank = self.rank
            self.rank += self.progress // 100
            self.progress = self.progress % 100
            if old_rank < 0 and self.rank >= 0:
                self.rank += 1
        if self.rank >= 8:
                self.rank = 8
                self.progress = 0

user = User(rank=-5)
user.inc_progress(8)
print(user.rank)
print(user.progress)
user.inc_progress(9)
print(user.rank)
print(user.progress)

        