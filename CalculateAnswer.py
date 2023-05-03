import BooleanFunctionSimplifier as BFS
import GetCoreMinterms as GCM

def runModel(variableNames, minterms):
    error = False
    coreMinterms = GCM.GetCoreMinterms(len(variableNames))
    for i in range(0,len(minterms)):
        if(minterms[i] not in coreMinterms):
            error = True
    if(error == False):
        simplifiedExpression = BFS.runProgram(coreMinterms, len(variableNames), variableNames, minterms)
        return simplifiedExpression
    else:
        return ''

