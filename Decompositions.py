from Matrix import Matrix
from Identity import IdentityMatrix as Idd
from Null import NullMatrix as Nul
from Scaling import ScalingMatrix as D
from Permutation import PermutationMatrix as P
from Combination import CombinationMatrix as L

def LR(A):
    Left = Idd().collapsed(A.n)
    Right = Idd() @ A

    for j in range(A.m - 1):
        r = j
        # Find pivot r
        while A[r, j] == 0:
            r += 1

        # permutate if necessary
        if r!=j:
            p = P(j, r)
            Left = Left @ p
            Right = p @ Right


        for i in range(j+1, A.n):
            q = -Right[i, j]/Right[j, j]
            Left = Left @ L(i, j, -q)
            Right = L(i, j, q) @ Right
            

    return (Left, Right)

if __name__ == "__main__":
    A = Matrix([[0, 5, 22/3],[4,2,1],[2,7,9]])
    res = LR(A)
    print(res[0], res[1])

