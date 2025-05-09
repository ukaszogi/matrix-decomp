from Matrix import Matrix

class CollapsibleMatrix(Matrix):
    def __init__(self, a=None):
        super().__init__([[]])
        self.__shape = ("uncollapsed", "uncollapsed")
        self.__default = a

    @property
    def n(self):
        return self.__shape[0]

    @property
    def m(self):
        return self.__shape[1]

    def __getitem__(self, index):
        return self.__default

    @property
    def isCollapsed(self):
        return type(self.__shape[0]) == int and type(self.__shape[1]) == int

    def __str__(self):
        return "Funky matrix"

    def collapse(self, q = None, n = None, m = None):
        if q and not n:
            # one arg alone -> square matrix
            return self.collapse(q, q)
        if q and n:
            # two unnamed args -> n x m
            return self.collapse(n = q, m = n)
        if n:
            self.__shape = (n, self.__shape[1])
        if m:
            self.__shape = (self.__shape[0], m)
        if type(self.__shape[0]) != int or type(self.__shape[1]) != int:
            return self
        if not q and not n and not m:
            # already collapsed
            return self.__collapsed
        
        # collapsing
        a = []
        for i in range(self.n):
            a.append([])
            for j in range(self.m):
                a[i].append(self[i, j])

        self.__collapsed = Matrix(a)
        return self.__collapsed

if __name__ == "__main__":
    print("Testing library Collapsible.py")

    c = CollapsibleMatrix()

    print(c, c.n, c.m )
    c.collapse(3)
    print(c)



