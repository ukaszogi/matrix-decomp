from Matrix import Matrix
from Collapsible import CollapsibleMatrix
import copy

class IdentityMatrix(CollapsibleMatrix):
    def __init__(self, factor = 1):
        super().__init__()
        self.__factor = factor

    def __getitem__(self, index):
        if type(index) == tuple and len(index) == 2:
            return int(index[0] == index[1])

    def __add__(self, other):
        print("Catched addition and optimized")
        if type(other) == Matrix and other.n == other.m:
            a = copy.deepcopy(other)
            for i in range(a.n):
                a[i, i] += self.__factor
        return a

    def __mul__(self, other):
        print("Catched multiplication and optimized")
        if type(other) == Matrix:
            return other
        if type(other) in (int, float):
            return IdentityMatrix(self.__factor * other)

    __rmul__ = __mul__
    __radd__ = __add__

    def __str__(self):
        return "I"

if __name__ == "__main__":
    print("Testing library Identity.py")

    idd = IdentityMatrix()
    # print(idd, idd.n, idd.m)

    a = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    print(a)
    print(idd, type(idd))
    print(idd * a)
    print(a * idd)
    print(idd + -a)
    print(idd - a)
    print(a - idd)
