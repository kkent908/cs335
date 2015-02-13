%module Solution
%{
#include "Solution.h"
  %}

%include "std_string.i"
%include "std_vector.i"
%include "std_set.i"
%include "std_map.i"

namespace std {
  %template(DoubleVector) vector<double>;
  %template(IntVector) vector<int>;
  %template(IntSet) set<int>;
  %template(UnsignedSet) set<unsigned>;
  %template(MapIntToFunction) map<int,FunctionPtr>;
}
using namespace std;

%nodefaultctor Solution;  // Disable the default constructor for class Solution


class Solution {
public:

  static SolutionPtr solution(MeshPtr mesh, BCPtr bc = Teuchos::null,
                              RHSPtr rhs = Teuchos::null, IPPtr ip = Teuchos::null);

  // ------------------------------DON'T TEST TOO COMPLICATED---------------------------------------
  int solve(); //Solves. Returns 0 on success; returns an error code otherwise.

  void addSolution(SolutionPtr soln, double weight,
		   bool allowEmptyCells = false, bool replaceBoundaryTerms = false); //Adds the specified Solution to this with weight weight: thisSoln += weight * soln.

  void addSolution(SolutionPtr soln, double weight,
		   set<int> varsToAdd, bool allowEmptyCells = false); //Adds the specified Solution to this with weight as in the other addSolution method, but this sum only applies to the variables specified in varsToAdd. For other variables, the values in "soon" <---- THIS MIGHT BE A TYPO FOR SOLN---- replace those in the this Solution object.

  void clear(); //Clears all solution values. (Leaves everything else intact.)
  int cubatureEnrichmentDegree(); //Returns the polynomial degree enrichment used when computing integrals.
  void setCubatureEnrichmentDegree(int value); //Sets the polynomial degree enrichment to use when computing integrals.
  double L2NormOfSolution(int trialID); //Takes the L^2 norm of the solution in the variable specified by trialID. (Zero for zero solutions; computes area if the solution has value 1.)
  void projectOntoMesh(const map<int, FunctionPtr > &functionMap);
  double energyErrorTotal();
  void setWriteMatrixToFile(bool value,const string &filePath);
  void setWriteMatrixToMatrixMarketFile(bool value,const string &filePath);
  void setWriteRHSToMatrixMarketFile(bool value, const string &filePath);
  MeshPtr mesh();
  BCPtr bc();
  RHSPtr rhs();
  IPPtr ip();
  void setBC( BCPtr );
  void setRHS( RHSPtr );
  void setIP( IPPtr );
  void save(string meshAndSolutionPrefix);
  static SolutionPtr load(BFPtr bf, string meshAndSolutionPrefix);
  void saveToHDF5(string filename);
  void loadFromHDF5(string filename);
 };


class SolutionPtr {
 public:
  Solution* operator ->();
};
