%module IP
%{
#include "IP.h"
%}

%include "std_map.i"


namespace std {
  %template(MapIntToFunction) map<int,FunctionPtr>;
}

using namespace std;


class IP{
public:
  IP();
  void addTerm(LinearTermPtr a);
  void addTerm(VarPtr v);
  LinearTermPtr evaluate(std::map< int, FunctionPtr> &varFunctions);

 %extend {
    LinearTermPtr evaluate(const map<int, FunctionPtr> &varFunctions) {
      map<int, FunctionPtr> varFunctionsCopy = varFunctions;
      return self->evaluate(varFunctionsCopy);
    }
  }



};
