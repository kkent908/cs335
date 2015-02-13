import PoissonFormulation
import Solution
import Mesh
import MeshFactory
import BC
import RHS
import IP
import Function
import Var
import VarFactory
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
        #how does this method even work

    def testAddSolution2(self):
        #create a new solution with mesh
        soln = Solution.Solution(mesh)
        Solution.addSolution(soln, 2.5)
        #how does this method even work

    def testClear(self):
        #create a new solution with mesh
        soln = Solution.Solution(mesh)
        Solution.clear()
        self.assertIsNotNone(soln)

    def testCubEnriDegr(self):
        soln = Solution.Solution(mesh)
        soln.setCubatureEnrichmentDegree(8)
        self.assertEquals(Solution.cubatureEnrichmentDegree(), 8)

    def tesSetCubatureEnrichmentDegree(self):
        soln = Solution.Solution(mesh)
        soln.setCubatureEnrichmentDegree(9)
        self.assertEquals(Solution.cubatureEnrichmentDegree(), 9)

    def testL2NormOfSolution(self):
        #make a bf, add a field variable, then get its id, pass it to L2Norm
        soln = Solution.Solution(mesh)
        vf = VarFactory.VarFactory()
        fv = vf.fieldVar("I like poop")
        self.assertEquals(soln.L2Norm(fv.ID()), 0.0)
        
    def testProjOntoMesh(self):
        soln = Solution.Solution(mesh)
        #I have not been able to understand this method 

    def testEnergyErrorTotal(self):
        soln = Solution.Solution(mesh)
        #when I tried to use this method it seg faulted on multiple occasions
        #what error are we measuring??
