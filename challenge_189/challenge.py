import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test.strip() != '':
            # Format the input
            inputList = test.split(" ")
            noOfFriends = int(inputList[0])
            friendHouses = [int(i) for i in inputList[1:]]
            # This list stores distances between Alice home and friend's
            minDistanceFromFriendHouses = []
            for shiftingHouseDistance in friendHouses:
                 tempDistances = [abs((friendHouseDistance - shiftingHouseDistance)) for friendHouseDistance in friendHouses]
                 minDistanceFromFriendHouses.append(sum(tempDistances))
            print min(minDistanceFromFriendHouses)

