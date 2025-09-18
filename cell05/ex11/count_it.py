# 42bangkok2025-discovery-piscine-coding-with-python

import sys

def count_it():
    params = sys.argv[1:]
    print(f"parameters: {len(params)}")
    for i in params:
        print(f"{i}, {len(i)}")
    
count_it()