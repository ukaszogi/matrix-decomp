import pytest

from Matrix import Matrix
from Identity import IdentityMatrix as Idd
from Null import NullMatrix as Nul
from Scaling import ScalingMatrix as D
from Permutation import PermutationMatrix as P
from Combination import CombinationMatrix as L

class TestMatrix:

    A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    At = Matrix([[1,4,7],[2,5,8],[3,6,9]])
    AAt = Matrix([[14, 32, 50],[32, 77, 122],[50, 122, 194]])

    B = Matrix([[0, 1, 4, 6],[8, 9, 10, 12]])

    def test_add_mul(self):
        assert self.A*4 == Matrix([[4,8,12],[16,20,24],[28,32,36]])
        # assert self.A*1.4 == Matrix([[1.4,2.8,4.2],[5.6,7.,8.4],[9.8,11.2,12.6]])
        assert (self.A + (-1 * self.A)) == Nul().collapsed(3)

        assert (self.B.n, self.B.m) == (2, 4)
                    
    def test_transpose(self):
        assert self.A.T == self.At
        self.A.transpose()
        assert self.A == self.At
        self.A.transpose()

    def test_num_matmul(self):
        assert self.A @ self.At == self.AAt

class TestCollapsable:
    A = Matrix([[1,2,3],[4,5,6],[7,8,9]])

    def test_identity(self):
        idd = Idd().collapsed(4)
        idd[2, 0] = 4
        print(idd, type(idd))
