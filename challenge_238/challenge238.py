import sys

def isCharsInTheString(charArr):
    checkString = "code"
    for i in checkString:
        if i not in charArr:
            return False
    return True


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test.strip() != '':
            matchCount = 0
            mainArr = [list(i.strip()) for i in test.split("|")]
            # Get the length of array
            innerMatrixLen = len(mainArr[0])
            outerMatrixLen = len(mainArr)
            # Start building the logic
            for iIndex, iVal in enumerate(mainArr):
                for jIndex, jVal in enumerate(iVal):
                    if jIndex < (innerMatrixLen - 1) and iIndex < (outerMatrixLen - 1):
                        if isCharsInTheString([mainArr[iIndex][jIndex], mainArr[iIndex][jIndex + 1], mainArr[iIndex + 1][jIndex], mainArr[iIndex + 1][jIndex + 1]]):
                            matchCount += 1
            print matchCount
