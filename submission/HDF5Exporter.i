%module HDF5Exporter
%{
#include "HDF5Exporter.h"
%}

%include "std_string.i"
%include "std_vector.i"
%include "VarFactory.i"
%include "Solution.i"

namespace std {
  %template(FunctionVector) vector<FunctionPtr>;
   %template(StringVector) vector<string>;
 }

using namespace std;

%nodefaultctor HDF5Exporter;  // Disable the default constructor for class HDF5Exporter

class HDF5Exporter {
 public:
  HDF5Exporter(MeshPtr mesh, string outputDirName="output", string outputDirSuperPath = ".");

  void exportFunction(FunctionPtr function, string functionName="function", double timeVal=0);

  void exportFunction(vector<FunctionPtr> functions, vector<string> functionNames, double timeVal=0);

  void exportSolution(SolutionPtr solution, VarFactory varFactory, double timeVal=0);
 };
