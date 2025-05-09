from Matrix import Matrix
from Collapsible import CollapsibleMatrix, matmulCondition, addCondition
import copy

class CombinationMatrix(CollapsibleMatrix):
    def __init__(self, i, j, m):
        super().__init__()
        self.__i = i
        self.__j = j
        self.__m = m
    
    def __getitem__(self, index):
        return self.__m if index == (self.__i, self.__j) else int(index[0] == index[1])

    def __add__(self, other):
        addCondition(self, other)

        # add optimalisation O(n)
        a = copy.deepcopy(other)
        for i in range(self.n):
            a[i, i] += 1
        a[self.__i, self.__j] += self.__m
        return a

    def __matmul__(self, other):
        matmulCondition(self, other)

        # matmul optimalisation O(m)
        a = copy.deepcopy(other)
        for j in range(a.m):
            a[self.__i, j] += self.__m * a[self.__j, j]
        return a

    def collapse(self, n = None, m = None):
        # collapse optimalisation
        # matrix only exist as a square
        p =  n if n else m if m else None
        return CollapsibleMatrix.collapse(self, n=p, m=p)

if __name__ == "__main__":
    print("Testing library Scaling.py")

    A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    L = CombinationMatrix(1, 0, -2)

    print(L @ A)
