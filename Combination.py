from Collapsible import CollapsibleMatrix

class CombinationMatrix(CollapsibleMatrix):
    def __init__(self, i, j, m):
        super().__init__()
        self.__i = i
        self.__j = j
        self.__m = m
    
    def __getitem__(self, index):
        return self.__m if index == (self.__i, self.__j) else int(index[0] == index[1])

    def collapse(self, n = None, m = None):
        # collapse optimalisation
        # matrix only exist as a square
        p =  n if n else m if m else None
        return CollapsibleMatrix.collapse(self, n=p, m=p)

if __name__ == "__main__":
    print("Testing library Scaling.py")

    L = CombinationMatrix(3, 1, 3)
    print(L.collapse(7))
