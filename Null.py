from Matrix import Matrix
from Collapsible import CollapsibleMatrix, matmulCondition, rmatmulCondition, addCondition
import copy

class NullMatrix(CollapsibleMatrix):
    def __init__(self):
        super().__init__()

    def __getitem__(self, index):
        if type(index) == tuple and len(index) == 2:
            return 0

    def __add__(self, other):
        addCondition(self, other)
        return other

    def __iadd__(self, other):
        # HACK: Edytowanie selfa, addCondition wewnątrz `other + self`
        self = other + self
        return self

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise ValueError(f"Cannot multiply types {type(self)} and {type(other)}")
        return self

    def __matmul__(self, other):
        matmulCondition(self, other)
        return self

    def __rmatmul__(self, other):
        rmatmulCondition(self, other)
        return self

    __rmul__ = __mul__
    __imul__ = __mul__
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

    nul = NullMatrix()
    nul += a.T 
    print(nul)
