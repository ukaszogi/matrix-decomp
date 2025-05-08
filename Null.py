from Matrix import Matrix
from Identity import IdentityMatrix

class NullMatrix(Matrix):
    def __init__(self):
        pass

    def __getitem__(self, index):
        if type(index) == tuple and len(index) == 2:
            return 0

    def __add__(self, other):
        print("Catched addition and optimized")
        if type(other) == Matrix:
            return other

    def __mul__(self, other):
        print("Catched multiplication and optimized")
        if type(other) in (Matrix, int, float):
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
