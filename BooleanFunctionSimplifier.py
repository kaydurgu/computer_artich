def runProgram(coreMinterms, numVariables, variableNames, minterms):
    minterms1 = findMinterms(minterms)  
    tabularForm = convertTabularForm(numVariables, minterms, coreMinterms)
    
    tabularForm1, checkList1, minterms2 = compareMinterms(tabularForm,numVariables, minterms1)
    tabularForm2, checkList2, minterms3 = compareMinterms(tabularForm1, numVariables, minterms2)
    
    minterms1 = unpackMinterms(minterms1)
    minterms3 = unpackMinterms(minterms3)
    
    tabularForm2, minterms3 = elimRepeats(tabularForm2, minterms3)
    
    primeImplicants, primeMinterms = findPrimeImplicants(tabularForm, tabularForm1, tabularForm2, checkList1, checkList2, minterms1, minterms2, minterms3)
    
    essentialImplicants, essentialMinterms = findEssentialImplicants(minterms1, primeMinterms, primeImplicants)
    
    mintermsNeeded = checkForMoreImplicants(essentialMinterms, minterms1)
    
    finalTabularForm = chooseMoreImplicants(essentialImplicants, mintermsNeeded, primeMinterms, primeImplicants)
    
    booleanExpression = tabularFormToExpression(finalTabularForm, variableNames)
    return booleanExpression

def findMinterms(minterms):
    finalMinterms = []
    for i in range(0,len(minterms)):
        finalMinterms.append(int(minterms[i].replace('m', '')))   
    return finalMinterms

def convertTabularForm(numVariables, minterms, coreMinterms):  
    tabularForm = []
    for x in range (0,len(minterms)):
        tabularForm.append(coreMinterms[minterms[x]])
    return tabularForm

def compareMinterms(tabularForm, numVariables, minterms1):
    similarities = numVariables - 1
    nextStep = []
    similarVal = 0
    checkList = []
    minterms2 = []
   
    for i in range (0,len(tabularForm)):   
        for x in range (i+1,len(tabularForm)):
            for z in range (0,numVariables):
                if(tabularForm[i][z] == tabularForm[x][z]): 
                    similarVal = similarVal + 1
            if(similarVal == similarities):
                minterms2.append([minterms1[i], minterms1[x]])
                checkList.append(tabularForm[i])
                checkList.append(tabularForm[x])
                nextStep.append(createImplicants(tabularForm[i], tabularForm[x], numVariables)) 
            similarVal = 0
    return nextStep, checkList, minterms2
     
def createImplicants(a, b, numVariables):
    mixMinterms = []
    for i in range (0,numVariables):
        if(a[i] != b[i]):
            mixMinterms.insert(i,'-')
        else:
            mixMinterms.insert(i,a[i])
    return mixMinterms

def unpackMinterms(minterms):
    unpackedMinterms = []
    unpackingList = []

    for x in range(0,len(minterms)):
        if(type(minterms[x]) is list):
            for y in range(0,len(minterms[x])):
                for z in range(0,len(minterms[x][y])):
                    unpackingList.append(minterms[x][y][z])  
            unpackedMinterms.append(unpackingList)
            unpackingList = []
        else:
            unpackingList.append(minterms[x])
            unpackedMinterms.append(unpackingList)
            unpackingList = []
                    
    
    return unpackedMinterms


def elimRepeats(tabularForm, minterms):
    finalTabularForm = []
    finalMinterms = []
    
    for x in range(0, len(tabularForm)):
        if(tabularForm[x] not in finalTabularForm):
            finalTabularForm.append(tabularForm[x])
            finalMinterms.append(minterms[x])

    return finalTabularForm, finalMinterms


def findPrimeImplicants(tabularForm, tabularForm1, tabularForm2, checkList1, checkList2, minterms1, minterms2, minterms3):
    primeImplicants = []
    primeMinterms = []

    for x in range(0, len(tabularForm)):
        if(tabularForm[x] not in checkList1):
            primeImplicants.append(tabularForm[x])
            primeMinterms.append(minterms1[x])
            
    for x in range(0, len(tabularForm1)):
        if(tabularForm1[x] not in checkList2):
            primeImplicants.append(tabularForm1[x])
            primeMinterms.append(minterms2[x])

    primeImplicants = primeImplicants + tabularForm2
    primeMinterms = primeMinterms + minterms3
    return primeImplicants, primeMinterms

def findEssentialImplicants(minterms1, primeMinterms, primeImplicants):
    similarities = {}
    essentialImplicants = []
    essentialMinterms = []
    
    for x in range(0, len(minterms1)): 
        similarities[minterms1[x][0]] = 0
   

    for x in range(0, len(primeMinterms)): 
        for y in range(0, len(primeMinterms[x])):
            for z in range(0,len(minterms1)):
                if(primeMinterms[x][y] == minterms1[z][0]):
                    similarities[primeMinterms[x][y]] = similarities[primeMinterms[x][y]] + 1

    for x in range(0,len(minterms1)):  
        if(similarities[minterms1[x][0]] == 1):
            for y in range(0,len(primeMinterms)):
                for z in range(0,len(primeMinterms[y])):
                    if(minterms1[x][0] == primeMinterms[y][z] and primeImplicants[y] not in essentialImplicants):
                        essentialImplicants.append(primeImplicants[y])
                        essentialMinterms.append(primeMinterms[y])
                        
    return essentialImplicants, essentialMinterms


def checkForMoreImplicants(essentialMinterms, minterms1):
    mintermsNeeded = []
    unpackingList = []

    for i in range(0,len(essentialMinterms)):
        for x in range(0,len(essentialMinterms[i])):
            if(essentialMinterms[i][x] not in unpackingList):
                unpackingList.append(essentialMinterms[i][x])

    for i in range(0,len(minterms1)):
        if(minterms1[i][0] not in unpackingList):
            mintermsNeeded.append(minterms1[i][0])
            
    return mintermsNeeded


def chooseMoreImplicants(essentialImplicants, mintermsNeeded, primeMinterms, primeImplicants):
    potentialMinterms = []
    finalTabularForm = essentialImplicants
    foundMinterm = False
    
    for x in range(0,len(mintermsNeeded)):
        for y in range(0,len(primeMinterms)):
            for z in range(0,len(primeMinterms[y])):
                if(mintermsNeeded[x] == primeMinterms[y][z]):
                    potentialMinterms.append(primeMinterms[y])

    for x in range(0,len(potentialMinterms)):
        if(potentialMinterms[x] == mintermsNeeded and primeImplicants[primeMinterms.index(potentialMinterms[x])] not in finalTabularForm):
            finalTabularForm.append(primeImplicants[primeMinterms.index(potentialMinterms[x])])
            foundMinterm = True

    if(foundMinterm == False and len(mintermsNeeded) > 0):
        for x in range(0,len(potentialMinterms)):
            for y in range(0,len(primeMinterms)):
                if(potentialMinterms[x] in primeMinterms[y]):
                    finalTabularForm.append(primeImplicants[primeMinterms.index(potentialMinterms[x])])
                    break
            
    return finalTabularForm

def tabularFormToExpression(finalTabularForm, variableNames):
    booleanExpression = ""
    
    for i in range(0,len(finalTabularForm)):
        for x in range(0,len(finalTabularForm[i])):
            if(finalTabularForm[i][x] == 0):
                booleanExpression = booleanExpression + '~' + variableNames[x]
                booleanExpression = booleanExpression + '&'
            elif(finalTabularForm[i][x] == 1):
                booleanExpression = booleanExpression + variableNames[x]
                booleanExpression = booleanExpression + '&'
        booleanExpression = booleanExpression[:-1]
        booleanExpression = booleanExpression + '|'
    booleanExpression = booleanExpression[:-1]
            
    return booleanExpression

