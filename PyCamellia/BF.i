%module BF
%{
#include "BF.h"
%}

%include "std_string.i"

class BF {
 public:
   BF( VarFactory varFactory );
   void addTerm( LinearTermPtr trialTerm, LinearTermPtr testTerm );
   void addTerm( VarPtr trialVar, LinearTermPtr testTerm );
   void addTerm( VarPtr trialVar, VarPtr testVar );
   void addTerm( LinearTermPtr trialTerm, VarPtr testVar);

   const string & testName(int testID);
   const string & trialName(int trialID);

   Camellia::EFunctionSpace functionSpaceForTest(int testID);
   Camellia::EFunctionSpace functionSpaceForTrial(int trialID);

   IPPtr graphNorm(double weightForL2TestTerms = 1.0);
   IPPtr naiveNorm(int spaceDim);

   bool isFluxOrTrace(int trialID);

   string displayString();
   LinearTermPtr testFunctional(SolutionPtr trialSolution);

   VarFactory varFactory();


   %extend {
     void addTerm(std::string name, int fs, int ID = -1) {
    return self->testVar(name, (Space)fs, ID);

   }

 };


class BFPtr {
public:
  BF* operator->();
};
