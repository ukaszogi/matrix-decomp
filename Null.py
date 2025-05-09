from Matrix import Matrix
from Collapsible import CollapsibleMatrix
import copy

class NullMatrix(CollapsibleMatrix):
    def __init__(self):
        super().__init__()

    def __getitem__(self, index):
        if type(index) == tuple and len(index) == 2:
            return 0

    def __add__(self, other):
        if type(other) != Matrix:
            raise ValueError(f"Cannot add types {type(self)} and {type(other)}")
        if (type(self.n) == int and self.n != other.n) or (type(self.m) == int and self.m != other.m):
            raise ValueError(f"Shapes don't match: {self._shape} != {other._shape}")

        self.collapse(other.n, other.m)
        return other

    def __iadd__(self, other):
        if type(other) != Matrix:
            raise ValueError(f"Cannot add types {type(self)} and {type(other)}")
        if (type(self.n) == int and self.n != other.n) or (type(self.m) == int and self.m != other.m):
            raise ValueError(f"Shapes don't match: {self._shape} != {other._shape}")

        # HACK: Edytowanie selfa
        self = other + self
        return self

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise ValueError(f"Cannot multiply types {type(self)} and {type(other)}")

        return self

    def __matmul__(self, other):
        if type(other) != Matrix:
            raise ValueError(f"Cannot multiply types {type(self)} and {type(other)}")

        self.collapse(m = other.n)
        return self

    def __rmatmul__(self, other):
        if type(other) != Matrix:
            raise ValueError(f"Cannot multiply types {type(self)} and {type(other)}")

        self.collapse(n = other.m)
        return self

    __rmul__ = __mul__
    __radd__ = __add__

    def __str__(self):
        if int not in (type(self.n), type(self.m)):
            return "0"

        return f"0_({self.n}x{self.m})"

if __name__ == "__main__":
    print("Testing library Null.py")

    a = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    print(a)
    
    nul = NullMatrix()
    print(nul, type(nul))
    print(nul @ a)
    print(nul + Matrix([[1,2,3]]))

    # BUG: Tu problemem jest, że najbliższa implementacja nul.__iadd__() jest w Matrix, a tam nie robi po prostu return other, tylko sprawdza shape i iteruje po elementach (nie iteruje, bo shape niefajny)
    nul = NullMatrix()
    nul += a.T 
    print(nul)
