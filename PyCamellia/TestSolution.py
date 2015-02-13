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

formulation = PoissonFormulation.PoissonFormulation(2, True)
bf = formulation.bf()
mesh = MeshFactory.MeshFactory_rectilinearMesh(bf, [1.0, 2.0], [3, 4], 10)

def testSolnConstr(self):
#create a new solution with mesh
soln = Solution.Solution(mesh)
self.assertEquals(soln.mesh().numActiveElements(), 12, "Testing Solution Constructor")

def testDupSolnConstr(self):
#create a new solution with mesh
soln = Solution.Solution(mesh)
solnDup = Solution.Solution(soln)
self.assertEquals(solnDup.mesh().numActiveElements(), 12, "Testing Solution Constructor")

def testAddSolution1(self):
#create a new solution with mesh
soln = Solution.Solution(mesh)
Solution.addSolution(soln, 2.5)

def testAddSolution2(self):
#create a new solution with mesh
soln = Solution.Solution(mesh)
Solution.addSolution(soln, 2.5)

def testClear(self)
#create a new solution with mesh
soln = Solution.Solution(mesh)
Solution.clear()
self.assertEquals(soln, null)

def testCubEnriDegr(self)

def tesSetCubatureEnrichmentDegree(self)
Solution.

def testL2NormOfSolution(self)
