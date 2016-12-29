from __future__  import division
import sys


def hslToRGB(hsl):
    temp = hsl.strip("HSL(").rstrip(")\n").split(",")
    H = int(temp[0])
    S = float(temp[1]) / 100
    L = float(temp[2]) / 100

    #225 0.89 0.3
    # Calculate C, X, m
    C = (1 - (abs((2 * L) - 1))) * S
    X = C * (1 - abs(float(H / 60) % 2 - 1))
    m = L - (C/2)

    # Now calculate intermediate RGB values
    if (H >= 0 and H <= 60):
        _R, _G, _B = C, X, 0
    elif (H >= 60 and H < 120):
        _R, _G, _B = X, C, 0
    elif (H >= 120 and H < 180):
        _R, _G, _B = 0, C, X
    elif (H >= 180 and H < 240):
        _R, _G, _B = 0, X, C
    elif (H >= 240 and H < 300):
      _R, _G, _B = X, 0, C
    elif (H >= 300 and H < 360):
        _R, _G, _B = C, 0, X
    #Calculate RGB
    R, G, B = (_R + m) * 255, (_G + m) * 255, (_B + m) * 255
    return "(%d,%d,%d)" % (round(R), round(G), round(B))

def hsvToRGB(hsv):
    temp = hsv.strip("HSV(").rstrip(")\n").split(",")
    H = int(temp[0])
    S = int(temp[1]) / 100
    V = int(temp[2]) / 100
    # Calculate C, X, m
    C = V * S
    X = C * (1 - abs((H / 60) % 2 - 1))
    m = V - C

    # Now apply the conversion formulae
    if (H >= 0 and H <= 60):
        _R, _G, _B = C, X, 0
    elif (H >= 60 and H < 120):
        _R, _G, _B = X, C, 0
    elif (H >= 120 and H < 180):
        _R, _G, _B = 0, C, X
    elif (H >= 180 and H < 240):
        _R, _G, _B = 0, X, C
    elif (H >= 240 and H < 300):
      _R, _G, _B = X, 0, C
    elif (H >= 300 and H < 360):
        _R, _G, _B = C, 0, X
    #Calculate RGB
    R, G, B = (_R + m) * 255, (_G + m) * 255, (_B + m) * 255
    return "(%d,%d,%d)" % (round(R), round(G), round(B))    


def cmykToRGB(cmyk):
    temp = cmyk.lstrip('(').strip().rstrip(')').split(',')
    C = float(temp[0])
    M = float(temp[1])
    Y = float(temp[2])
    K = float(temp[3])
    R = round(255 * (1-C) * (1-K))
    G = round(255 * (1-M) * (1-K))
    B = round(255 * (1-Y) * (1-K))
    return "(%d,%d,%d)" % (int(R), int(G), int(B))

def hexToRGB(hexString):
    hexString = hexString[1:]
    x = int(hexString[:2], 16)
    y = int(hexString[2:4], 16)
    z = int(hexString[4:6], 16)
    return "(%s,%s,%s)" % (x, y, z) 

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test.strip() != '':
            finalString = "RGB"
            if ("HSL" in test):
                finalString += hslToRGB(test)
            elif ("HSV" in test):
                finalString += hsvToRGB(test)
            elif ("#" in test):
                finalString += hexToRGB(test)
            else:
                # This is CMYK
                finalString += cmykToRGB(test)
            print finalString
