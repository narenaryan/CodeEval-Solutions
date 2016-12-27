import sys

codelMap = {
	'y' : 'a',
	'n' : 'b',
	'f' : 'c',
	'i' : 'd',
	'c' : 'e',
	'w' : 'f',
	'l' : 'g',
	'b' : 'h',
	'k' : 'i',
	'u' : 'j',
	'o' : 'k',
	'm' : 'l',
	'x' : 'm',
	's' : 'n',
	'e' : 'o',
	'v' : 'p',
	'z' : 'q',
	'p' : 'r',
	'd' : 's',
	'r' : 't',
	'j' : 'u',
	'g' : 'v',
	'a' : 'y',
	'q' : 'z',
	't' : 'w',
	'h' : 'x'
}
with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	if test.strip() != '':
	    	output_string = ''
	    	for char in test.strip():
	    		if char == ' ':
	    			output_string += ' '
	    		else:
	    			output_string += codelMap[char]
	    	print output_string
        