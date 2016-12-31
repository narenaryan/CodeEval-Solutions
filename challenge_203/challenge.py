import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        matchedIndexes = []
        for index, char in enumerate(test):
            if (char == "<"):
                try:
                    if (test[index: index + 5] == "<--<<"):
                        matchedIndexes.append(index)
                except:
                    pass
            if (char == ">"):
                try:
                    if (test[index: index + 5] == ">>-->"):
                        matchedIndexes.append(index)
                except:
                    pass
        print len(matchedIndexes)

