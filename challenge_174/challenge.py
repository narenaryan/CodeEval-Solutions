import sys

slangWords = [", yeah!", 
              ", this is crazy, I tell ya.",
              ", can U believe this?",
              ", eh?",", aw yea.",
              ", yo.",
              "? No way!",
              ". Awesome!"
              ]

def returnSlangWord():
    """
    A circular array for yielding slang words 
    """
    index = -1
    while True:
        index += 1
        yield slangWords[index % len(slangWords)]

with open(sys.argv[1], 'r') as test_cases:
    # These are the variables global for all the lines
    punctuationOccurrenceCount = 0
    slangGenerator = returnSlangWord()
    for test in test_cases:
        # If test case is not an empty line process further
        if test.strip() != "":
            outputString = ''
            for char in test:
                # Check for every character that matches given criteria
                if (char in ['.', '?', '!']):
                    punctuationOccurrenceCount += 1
                    if (punctuationOccurrenceCount % 2 == 0):
                        outputString += slangGenerator.next()
                    else:
                        # Don't append slang. Just append character as it is
                        outputString += char    
                # If not just append it to the string
                else:
                    outputString += char
            print outputString.strip()  
