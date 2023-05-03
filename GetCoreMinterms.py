
def GetCoreMinterms(numVariables):
    coreMinterms = {'m0':[0]}
    numMinterms = pow(2, numVariables)  

    with open("BinaryNumbers.txt", 'r', encoding = 'utf-8') as f:
        for i in range(1,numMinterms):
            line = f.readline()
            line = list(line.strip('\n'))
            for x in range(0, len(line)):
                line[x] = int(line[x])
            key = 'm' + str(i)
            coreMinterms[key] = line

    for i in range(0,len(coreMinterms)): 
        key = 'm' + str(i)
        if(len(coreMinterms[key]) != numVariables):
            diff = numVariables - len(coreMinterms[key])
            for x in range(0,diff):
                coreMinterms[key].insert(0,0)
    return coreMinterms


