# 42bangkok2025-discovery-piscine-coding-with-python

import sys

def parameter_matching():
    if (len(sys.argv) != 2):
        return "none!"
    
    text = input("What was parameter? ")
    if (text == sys.argv[1]):
        return "Good job!"
    else:
        return "Nope, sorry..."
    
print(parameter_matching())