import PoissonFormulation
import Solution
import Mesh
import MeshFactory
import BC
import RHS
import IP
import Function
import unittest

class TestSolution(unittest.TestCase):
    """Test Solution's methods"""

def testSolnConstr1(self):
formulation = PoissonFormulation.PoissonFormulation(2, True)
bf = formulation.bf()
mesh = MeshFactory.MeshFactory_rectilinearMesh(bf, [1.0, 2.0], [3, 4], 10)

#create a new solution with mesh
soln = Solution.Solution(mesh)
self.assertEquals(soln.mesh().numActiveElements(), 12, "Testing Solution Constructor")
        


    #def testAddSolution(self):
    """void addSolution(Teuchos::RCP<Solution> soln, double weight,
		   bool allowEmptyCells = false, bool replaceBoundaryTerms = false);"""
