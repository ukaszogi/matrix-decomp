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

    B = Matrix([[14, 32, 50],[32, 77, 122],[50, 122, 194]])

    def test_transpose(self):
        assert self.A.T == self.At
        self.A.transpose()
        assert self.A == self.At
        self.A.transpose()

    def test_num_matmul(self):
        assert self.A @ self.At == self.B
                
