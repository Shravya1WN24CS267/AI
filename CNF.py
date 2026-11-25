
import re

def fol_to_cnf(expr):
    print("\nOriginal FOL:", expr)

    # Step 1: Eliminate implication
    expr = re.sub(r'(\w+)\s*->\s*(\w+)',
                  r'(NOT \1 OR \2)', expr)
    print("\nStep 1 - Eliminate implication:")
    print(expr)

    # Step 2: Remove universal quantifier
    expr = re.sub(r'FORALL\s+\w+\s*', '', expr)
    print("\nStep 2 - Remove universal quantifier:")
    print(expr)

    # Step 3: Remove extra brackets
    expr = expr.replace("((", "(").replace("))", ")")
    print("\nStep 3 - CNF expression:")
    print(expr)

    return expr


print("FIRST ORDER LOGIC TO CNF CONVERSION")
print("-----------------------------------")

print("Use FORALL x and implication ->")
fol = input("Enter FOL expression: ")

result = fol_to_cnf(fol)

print("\nFinal CNF:", result)
