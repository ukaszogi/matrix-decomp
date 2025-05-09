from Matrix import Matrix
from Collapsible import CollapsibleMatrix, matmulCondition, rmatmulCondition, addCondition
import copy

class PermutationMatrix(CollapsibleMatrix):
    def __init__(self, i, j):
        super().__init__()
        self.__i = i
        self.__j = j

    def __getitem__(self, index):
        # TODO: Proszę posprzątać pokój!
        return int(
             (index[0] == index[1]) # diagnoal?
        and (index[0] != self.__i and index[0] != self.__j) # i = __i and j = __j
        or not (index[0] != self.__i and index[0] != self.__j) # or maybe i = __i and j = __j
        and (index[0] == self.n-index[1]-1) #but on anti-diagonal?
)

    def __add__(self, other):
        addCondition(self, other)

        # add optimalisation O(n)
        a = copy.deepcopy(other)
        for i in range(self.n):
            if i == self.__i:
                a[i, self.__j] += 1
                continue
            elif i == self.__j:
                a[i, self.__i] += 1
                continue

            a[i, i] += 1
        return a

    def __matmul__(self, other):
        matmulCondition(self, other)

        # matmul optimalisation O(1)
        a = copy.deepcopy(other)
        a[self.__i,:], a[self.__j,:] = a[self.__j,:], a[self.__i,:]
        return a

    def __rmatmul__(self, other):
        rmatmulCondition(self, other)

        # rmatmul optimalisation O(1)
        a = copy.deepcopy(other)
        a[:,self.__i], a[:,self.__j] = a[:,self.__j], a[:,self.__i]
        return a

    def collapse(self, n = None, m = None):
        # collapse optimalisation
        # matrix only exist as a square
        p =  n if n else m if m else None
        return CollapsibleMatrix.collapse(self, n=p, m=p)

if __name__ == "__main__":
    print("Testing library Permutation.py")

    P = PermutationMatrix(2, 4)
    print(P.collapse(7))

    A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    A[1,:], A[2,:] = A[2,:], A[1,:]
    print(A)
    print(PermutationMatrix(1, 2) @ A)
