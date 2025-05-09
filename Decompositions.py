from Matrix import Matrix
from Identity import IdentityMatrix as Idd
from Null import NullMatrix as Nul
from Scaling import ScalingMatrix as D
from Permutation import PermutationMatrix as P
from Combination import CombinationMatrix as L

def LR(A):
    Q = Idd().collapse(A.n).collapsed
    Ptab = []

    for j in range(A.m - 1):
        print(A)
        r = j
        # Find pivot r
        while A[r, j] == 0:
            r += 1

        # permutate if necessary
        if r!=j:
            p = P(j, r)
            A = p @ A
            Ptab.append(p)
        else:
            Ptab.append(Idd().collapse(A.n).collapsed)

        for i in range(j+1, A.n):
            q = -A[i, j]/A[j, j]
            print(j, i, q)
            Q[i, j] = -q
            A = L(i, j, q) @ A
            

    return (Q, A)

if __name__ == "__main__":
    A = Matrix([[0, 5, 22/3],[4,2,1],[2,7,9]])
    res = LR(A)
    print(res[0] @ res[1])

