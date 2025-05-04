class User:

    rank = -8
    progress = 0

    def inc_progress(self, rank):
        if self.rank == rank:
            self.progress += 3
        elif self.rank - 1 == rank:
            self.progress += 1
        elif self.rank < rank:
            d = rank - self.rank
            self.progress += 10 * d * d
        else:
            return

        if self.progress >= 100:
            self.rank += 1
            if self.rank == 0:
                self.rank = 1
            self.progress -= 100
