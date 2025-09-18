# 42bangkok2025-discovery-piscine-coding-with-python/cell03/ex03/advanced_mult.py

def advanced_mult():
    for i in range(11):
        loop_inside = ""
        for j in range(11):
            loop_inside += str(i * j) + " "
        print(f"Table de {i}: {loop_inside}")

advanced_mult()
