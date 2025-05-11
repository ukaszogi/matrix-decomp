import copy

class Matrix:
    def __init__(self, a):
        self.__a = a
        self._shape = (len(a), len(a[0]))

    @property
    def n(self):
        return self._shape[0]

    @property
    def m(self):
        return self._shape[1]

    def __iter__(self):
        for row in self.__a:
            yield row

    def __getitem__(self, index):
        # TODO: [1, :] ma zwrócić [[a, b, c]] a [:, 1] -> [[a], [b], [c]] 
        if type(index) == tuple and len(index) == 2:
            return self.__a[index[0]][index[1]]

        raise ValueError(f"Advanced indcies not supported yet")

    def __setitem__(self, index, a):
        self.__a[index[0]][index[1]] = a

    def __eq__(self, other):
        if self._shape != other._shape:
            return False
        for i in range(self.n):
            for j in range(self.m):
                if self[i, j] != other[i, j]:
                    return False
        return True

    def __add__(self, other):
        if type(other) != Matrix:
            raise ValueError(f"Cannot add types {type(self)} and {type(other)}")
        if other._shape != self._shape:
            raise ValueError(f"Shapes don't match: {self._shape} != {other._shape}")

        a = copy.deepcopy(self)
        for (i, row) in enumerate(other):
            for (j, num) in enumerate(row):
                a[i, j] += num

        return a

    def __iadd__(self, other):
        if type(other) != Matrix:
            raise ValueError(f"Cannot add types {type(self)} and {type(other)}")
        if other._shape != self._shape:
            raise ValueError(f"Shapes don't match: {self._shape} != {other._shape}")

        for (i, row) in enumerate(other):
            for (j, num) in enumerate(row):
                self[i, j] += num

        return self

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise ValueError(f"Cannot multiply types {type(self)} and {type(other)}")

        a = copy.deepcopy(self)
        for (i, row) in enumerate(a):
            for (j, num) in enumerate(row):
                a[i, j] *= other
        return a

    def __imul__(self, other):
        if type(other) not in (int, float):
            raise ValueError(f"Cannot multiply types {type(self)} and {type(other)}")

        for (i, row) in enumerate(self):
            for (j, num) in enumerate(row):
                self[i, j] *= other
        return self

    def __matmul__(self, other):
        if Matrix not in type(other).__mro__:
            raise ValueError(f"Cannot multiply types {type(self)} and {type(other)}")

        if self.m != other.n:
            raise ValueError(f"Shapes don't match: {self._shape} and {other._shape} don't share inner component ({self.m != other.n})")

        a = []
        for i in range(self.n):
            a.append([])
            for j in range(other.m):
                a[i].append(0)
                for p in range(self.m):
                    a[i][j] += self[i, p]*other[p, j]

        return Matrix(a)

    def __rmatmul__(self, other):
        return other.__matmul__(self)

    __rmul__ = __mul__
    __neg__ = lambda self: self * -1
    __sub__ = lambda self, other: self + -other
    __rsub__ = lambda self, other: other + -self

    def transpose(self):
        self.__a = [[self[j, i] for j in range(self.n)] for i in range(self.m)]
        self._shape = self._shape[::-1]
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
        s += '] ' + str(self._shape) + '\n'
        return s


if __name__ == "__main__":
    print("Testing library Matrix.py")

    A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    print(A)
    A.transpose()
    print(A)

    print(A*4)
    print(A*1.4)

    print(A.T)

    print(A + (-1 * A))

    print(A[1,1])

    C = Matrix([[0, 1, 4, 6],[8, 9, 10, 12]])
    print(C)
    C.transpose()
    print(C)
    print(C.n, C.m)

    print(A @ A.T)

    A += Matrix([[0,0,1],[0,0,1],[0,0,1]])
    print(A)

    B = Matrix([[1,2,3,2],[4,10,0,1],[8,0,-3,-16]])

    print(A, B, C)
    print(A @ B @ C)
