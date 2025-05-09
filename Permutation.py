from Collapsible import CollapsibleMatrix

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

    def collapse(self, n = None, m = None):
        # collapse optimalisation
        # matrix only exist as a square
        p =  n if n else m if m else None
        return CollapsibleMatrix.collapse(self, n=p, m=p)

if __name__ == "__main__":
    print("Testing library Permutation.py")

    P = PermutationMatrix(2, 4)
    print(P.collapse(7))
