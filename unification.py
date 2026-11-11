
# Unification in First Order Logic (FOL)

# Function to check whether a term is a variable
def is_variable(x):
    return x in ['x', 'y', 'z']


# Function to perform unification
def unify(expr1, expr2):

    # Check predicate names
    if expr1[0] != expr2[0]:
        return None

    # Check number of arguments
    if len(expr1) != len(expr2):
        return None

    substitution = {}

    # Compare corresponding arguments
    for i in range(1, len(expr1)):

        a = expr1[i]
        b = expr2[i]

        # If both are identical
        if a == b:
            continue

        # If first argument is a variable
        elif is_variable(a):
            if a in substitution:
                if substitution[a] != b:
                    return None
            else:
                substitution[a] = b

        # If second argument is a variable
        elif is_variable(b):
            if b in substitution:
                if substitution[b] != a:
                    return None
            else:
                substitution[b] = a

        # If both are different constants
        else:
            return None

    return substitution


# Main program
expr1 = ("Eats", "x", "Apple")
expr2 = ("Eats", "Riya", "y")

print("Expression 1:", expr1)
print("Expression 2:", expr2)

result = unify(expr1, expr2)

if result is not None:
    print("\nUnification Successful!")
    print("Substitution:", result)

    # Apply substitutions
    unified = []

    for term in expr1:
        if term in result:
            unified.append(result[term])
        else:
            unified.append(term)

    print("Unified Expression:", tuple(unified))

else:
    print("\nUnification Failed!")
