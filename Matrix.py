import copy

class Matrix:
    def __init__(self, a):
        self.__a = a
        if a == [[]]:
            self.__shape = (0, 0)
        else:
            self.__shape = (len(a), len(a[0]))

    @property
    def n(self):
        return self.__shape[0]

    @property
    def m(self):
        return self.__shape[1]

    def __iter__(self):
        for row in self.__a:
            yield row

    def __getitem__(self, index):
        # TODO:
        # - [1, :] ma zwrócić [[a, b, c]] a [:, 1] -> [[a], [b], [c]] 
        if type(index) == tuple and len(index) == 2:
            return self.__a[index[0]][index[1]]

        raise ValueError(f"Advanced indcies not supported yet")

    def __setitem__(self, index, a):
        self.__a[index[0]][index[1]] = a

    def __add__(self, other):
        if type(other) != Matrix:
            raise ValueError(f"Cannot add types {type(self)} and {type(other)}")
        if other.__shape != self.__shape:
            raise ValueError(f"Shapes don't match: {self.__shape} != {other.__shape}")

        a = copy.deepcopy(self)
        for (i, row) in enumerate(other.__a):
            for (j, num) in enumerate(row):
                a[i, j] += num

        return a

    def __iadd__(self, other):
        if type(other) != Matrix:
            raise ValueError(f"Cannot add types {type(self)} and {type(other)}")
        if other.__shape != self.__shape:
            raise ValueError(f"Shapes don't match: {self.__shape} != {other.__shape}")

        for (i, row) in enumerate(other.__a):
            for (j, num) in enumerate(row):
                self[i, j] += num

        return self

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise ValueError(f"Cannot multiply types {type(self)} and {type(other)}")

        a = copy.deepcopy(self)
        for i in range(len(a.__a)):
            for j in range(len(a.__a[i])):
                a[i, j] *= other
        return a

    def __imul__(self, other):
        if type(other) not in (int, float):
            raise ValueError(f"Cannot multiply types {type(self)} and {type(other)}")

        for i in range(len(a.__a)):
            for j in range(len(a.__a[i])):
                self[i, j] *= other
        return self

    def __matmul__(self, other):
        if type(other) != Matrix:
            raise ValueError(f"Cannot multiply types {type(self)} and {type(other)}")

        if self.m != other.n:
            raise ValueError(f"Shapes don't match: {self.__shape} and {other.__shape} don't share inner component ({self.m != other.n})")

        a = []
        for i in range(self.n):
            a.append([])
            for j in range(other.m):
                a[i].append(0)
                for p in range(other.n):
                    a[i][j] += self[i, p]*other[p, j]

        return Matrix(a)

    __rmul__ = __mul__
    __neg__ = lambda self: self * -1
    __sub__ = lambda self, other: self + -other
    __rsub__ = lambda self, other: other + -self

    def transpose(self):
        a = []
        for (i, row) in enumerate(self.__a):
            for (j, num) in enumerate(row):
                if i==0:
                    a.append([])
                a[j].append(num)
        self.__a = a
        self.__shape = self.__shape[::-1]
        return self

    @property
    def T(self):
        return copy.deepcopy(self).transpose()

    def __str__(self):
        s = "["
        for (i, row) in enumerate(self.__a):
            if i:
                s += ' '
            s += str(row)
            if i != len(self.__a) - 1:
                s += '\n'
        s += '] ' + str(self.__shape) + '\n'
        return s


if __name__ == "__main__":
    print("Testing library Matrix.py")

    a = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    print(a)

    print(a*4)
    print(a*1.4)

    print(a.T)

    print(a + (-1 * a))

    print(a[1,1])

    b = Matrix([[0, 1, 4, 6],[8, 9, 10, 12]])
    print(b)
    b.transpose()
    print(b)
    print(b.n, b.m)

    print(a @ a.T)

    a += Matrix([[0,0,1],[0,0,1],[0,0,1]])
    print(a)
