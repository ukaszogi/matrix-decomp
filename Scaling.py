from Matrix import Matrix
from Collapsible import CollapsibleMatrix, matmulCondition, addCondition
import copy

class ScalingMatrix(CollapsibleMatrix):
    def __init__(self, i, m):
        super().__init__()
        self.__i = i
        self.__m = m

    def __getitem__(self, index):
        return int(index[0] == index[1]) * (self.__m if index[0] == self.__i else 1)

    def __add__(self, other):
        addCondition(self, other)

        # add optimalisation O(m)
        a = copy.deepcopy(other)
        for i in range(self.n):
            a[i, i] += m if i == self.__i else 1
        return a

    def __matmul__(self, other):
        matmulCondition(self, other)

        # matmul optimalisation O(m)
        a = copy.deepcopy(other)
        for j in range(a.m):
            a[self.__i, j] *= self.__m
        return a

    def collapse(self, n = None, m = None):
        # collapse optimalisation
        # matrix only exist as a square
        p =  n if n else m if m else None
        return CollapsibleMatrix.collapse(self, n=p, m=p)

if __name__ == "__main__":
    print("Testing library Scaling.py")

    D = ScalingMatrix(2, -4)
    # print(D.collapse(7))

    a = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    print (D @ a)
    print (D)
    print (D.collapse())
