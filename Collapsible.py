from Matrix import Matrix

def addCondition(a, b):
    if type(b) != Matrix:
        raise ValueError(f"Cannot add types {type(a)} and {type(b)}")
    if a.collapsed:
        if a._shape != b._shape:
            raise ValueError(f"Shapes don't match: {a._shape} != {b._shape}")
        return
    # updating shapes if applicable
    elif self.n == other.n:
        self.collapse(m = other.m)
    elif self.m == other.m:
        self.collapse(n = other.n)
    elif self._shape == ("?", "?"):
        self.collapse(other.n, other.m)

def matmulCondition(a, b):
    if a.m == "?":
        # invoking child-collapse if exists
        a.collapse(m = b.n)

    elif a.m != b.n:
        raise ValueError(f"Shapes don't match: {a._shape} and {b._shape} don't share inner component ({a.m != b.n})")

def rmatmulCondition(a, b):
    if a.n == "?":
        # invoking child-collapse if exists
        a.collapse(n = b.m)

    elif a.n != b.m:
        raise ValueError(f"Shapes don't match: {b._shape} and {a._shape} don't share inner component ({b.m != a.n})")

class CollapsibleMatrix(Matrix):
    def __init__(self, a=None):
        super().__init__([[]])
        self._shape = ("?", "?")
        self.__default = a
        self.__collapsed = None

    def __getitem__(self, index):
        return self.__default

    @property
    def isCollapsed(self):
        return bool(self.__collapsed)

    @property
    def collapsed(self):
        if "?" not in self._shape:
            return self.collapse()
        if not self.__collapsed:
            return lambda *args: self.collapse(*args).collapsed
            # raise ValueError("Not collapsed yet")
        return self.__collapsed

    def __add__(self, other):
        # if I'm here, there is no optimalisation implemented yet
        addCondition(self, other)

        # as a last resort defaulting to numerical O(n^2)
        return Matrix.__matmul__(self, other)

    def __matmul__(self, other):
        # if I'm here, there is no optimalisation implemented yet
        matmulCondition(self, other)

        # as a last resort defaulting to numerical O(n^3)
        return Matrix.__matmul__(self, other)

    def __str__(self):
        return "Funky matrix"

    def collapse(self, q = None, n = None, m = None):
        if self.__collapsed:
            #already collapsed
            return self.__collapsed

        if q and not n:
            # shorthand: one arg alone -> square matrix
            return self.collapse(q, q)
        elif q and n:
            # shorthand: two unnamed args -> n x m
            return self.collapse(n = q, m = n)

        #add information to the shape
        if n:
            if self.n != "?":
                raise ValueError(f"Tried to collapse already collapsed dimension (how?)")
            self._shape = (n, self._shape[1])
        if m:
            if self.m != "?":
                raise ValueError(f"Tried to collapse already collapsed dimension (how?)")
            self._shape = (self._shape[0], m)

        if n or m:
            # not called to collapse
            return self

        # ready and called for collapse
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

    # c = CollapsibleMatrix()
    #
    # print(c, c.n, c.m )
    # c.collapse(3)
    # print(c)
    # print(c.collapsed)

    c = CollapsibleMatrix()
    print(c.collapsed)


