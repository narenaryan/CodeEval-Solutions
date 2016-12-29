import sys

def getChange(money, coinBox):
    if (money == 0): return 1
    elif (len(coinBox) == 0 or money < 0): return 0
    else: return getChange(money - coinBox[0], coinBox) + getChange(money, coinBox[1:]) 


coinBox = [50, 25, 10, 5, 1]
with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        money = int(test.strip())
        print getChange(money, coinBox)
