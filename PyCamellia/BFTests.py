import BF
import VarFactory
import Var
import LinearTerm
import Function
import IP
import unittest
import Solution
import MeshFactory
import Mesh
import PoissonFormulation

class Tests(unittest.TestCase):

#Test the method testName()
	def testTestName(self):

		vf = VarFactory.VarFactory()
		myVar = vf.testVar("identify me 1", 1)
		myVar2 = vf.testVar("identify me 2", 1);
		i = myVar2.ID();
	
		bf = BF.BF(vf);
		self.assertEqual(bf.testName(i), "identify me 2", "testName()");

	def testTrialName(self):
		vf = VarFactory.VarFactory();
		myVar = vf.fieldVar("identify me");
		myVar2 = vf.fieldVar("identify me 2");
		i = myVar2.ID();

		bf = BF.BF(vf);
		self.assertEqual(bf.trialName(i), "identify me 2", "trialName()");

#Test the method
	def testAddTerm(self):

f = Function.Function_xn(1);
g = Function.Function_yn(1);
vf = VarFactory.VarFactory();
u = vf.fieldVar("field");
v = vf.testVar("test", Var.HGRAD);
bf = BF.BF_bf(vf);
lt = 1.0 * u;
lt2 = 1.0 * v;
bf.addTerm(lt, lt2)
	

mesh = MeshFactory.MeshFactory_rectilinearMesh(bf, [1.0, 1.0], [1, 1], 10)


soln = Solution.Solution_solution(mesh)
soln.projectOntoMesh({u.ID() : f})
lt3 = bf.testFunctional(soln)

h = lt3.evaluate({v.ID() : g})

result = h.evaluate(5.0, 6.0);



		


		#FunctionPtr
h = lt.evaluate({u.ID() : f});

i = lt.evaluate({v.ID() : g});

	def testIsFluxOrTrace(self):
		vf = VarFactory.VarFactory();
		myVar = vf.fluxVar("identify me");
		myVar2 = vf.traceVar("hey");
		myVar3 = vf.fieldVar("hi");
		i = myVar.ID();
		j = myVar2.ID();
		k = myVar3.ID();

		bf = BF.BF(vf);
		self.assertEqual(bf.isFluxOrTrace(i), True, "test isFluxOrTrace");
		self.assertEqual(bf.isFluxOrTrace(j), True, "test isFluxOrTrace");
		self.assertEqual(bf.isFluxOrTrace(k), False, "test isFluxOrTrace");


	#just make sure this method runs successfully.
	def testGraphNorm(self):
		
		vf = VarFactory.VarFactory();
		bf = BF.BF(vf);
		bf.addTerm(lt, lt2);

		ip = bf.graphNorm();

	#just make sure this method runs successfully.
	def testNaieveNorm(self):
		vf = VarFactory.VarFactory();
		bf = BF.BF(vf);
		bf.naieveNorm(lt, lt2);

		ip = bf.graphNorm();


	def testVarFactory(self):


		
	

		vf = VarFactory.VarFactory();
		v = vf.fieldVar("hi");
		u = vf.fieldVar("field");
		uID = u.ID();
	
		bf = BF.BF(vf);
	
		vfCopy = bf.varFactory();
		uCopy = vfCopy.trial(uID);
		uIDCopy = uCopy.ID();

		self.assertEqual(uID, uIDCopy, "testing varFactory()");

if (__name__ == '__main__'):
  unittest.main()


	
