from Matrix import Matrix
from Identity import IdentityMatrix

class NullMatrix(Matrix):
    def __init__(self):
        pass

    def __getitem__(self, index):
        if type(index) == tuple and len(index) == 2:
            return 0

    def __add__(self, other):
        if type(other) == Matrix and other.n == other.m:
            a = copy.deepcopy(other)
            for i in range(a.n):
                a[i, i] += self.__factor
        return a

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise ValueError(f"Cannot multiply types {type(self)} and {type(other)}")

        return self

    def __matmul__(self, other):
        if type(other) != Matrix:
            raise ValueError(f"Cannot multiply types {type(self)} and {type(other)}")

        return self

    __rmul__ = __mul__
    __radd__ = __add__

    def __str__(self):
        return "0"

if __name__ == "__main__":
    print("Testing library Null.py")

    a = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    print(a)
    
    nul = NullMatrix()
    print(nul, type(nul))
    print(nul * a)
    print(a * nul)

    # TODO: mnożenie 0 z 1
    idd = IdentityMatrix()
    print(nul * idd)
    print(idd * nul)
