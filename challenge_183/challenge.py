import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        grid = [list(i.strip()) for i in test.split(",")]
        cavitiesCounts = []
        for row in grid:
            temp = 0
            for column in row:
                if column == "Y":
                    break
                elif (column == "."):
                    temp += 1
            cavitiesCounts.append(temp)
        print min(cavitiesCounts)
