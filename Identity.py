from Matrix import Matrix
from Collapsible import CollapsibleMatrix
import copy

class IdentityMatrix(CollapsibleMatrix):
    def __init__(self, factor = 1):
        super().__init__()
        self.__factor = factor

    def __getitem__(self, index):
        if type(index) == tuple and len(index) == 2:
            return self.__factor if index[0] == index[1] else 0

    def __add__(self, other):
        if type(other) != Matrix:
            raise ValueError(f"Cannot add types {type(self)} and {type(other)}")
        if other.n != other.m:
            raise ValueError(f"Shapes don't match: {self._shape} != {other._shape}")

        a = copy.deepcopy(other)
        for i in range(a.n):
            a[i, i] += self.__factor

        self.collapse(other.n)
        return a

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise ValueError(f"Cannot multiply types {type(self)} and {type(other)}")

        return IdentityMatrix(self.__factor * other)

    def __imul__(self, other):
        if type(other) not in (int, float):
            raise ValueError(f"Cannot multiply types {type(self)} and {type(other)}")

        self.__factor *= other
        return self

    def __matmul__(self, other):
        if type(other) != Matrix:
            raise ValueError(f"Cannot multiply types {type(self)} and {type(other)}")

        self.collapse(other.n)
        return other * self.__factor

    __radd__ = __add__
    __rmul__ = __mul__
    __rmatmul__ = __matmul__

    def __str__(self):
        return f"I{f"_{self.n}" if self.isCollapsed else ""}"

if __name__ == "__main__":
    print("Testing library Identity.py")

    idd = IdentityMatrix()
    # print(idd, idd.n, idd.m)

    a = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    print(a)
    print(idd, type(idd))
    print(idd @ a)
    print(idd)
    # print(a @ idd)
    # print(idd + -a)
    # print(idd - a)
    # print(a - idd)
    #
    print(id2 := IdentityMatrix(2).collapse(3))
    print(type(id2))
    print(type(idd.collapse()))

    idd = IdentityMatrix()
    idd @ a
    print(idd)

    # BUG: Tu problemem jest, że najbliższa implementacja idd.__iadd__() jest w Matrix, a tam jak ciągnie definicję __getitem__, to tą Matrixową, czyli __a[][], a idd ma inną (czyli factor * i==j)
    idd += a.T
    print(idd)
