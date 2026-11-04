from itertools import product

def implies(a, b):
    return not a or b

def truth_table():
    print("P Q R | Q->P | P->~Q | Q|R | KB")
    print("-----------------------------------")

    models = []

    for P, Q, R in product([False, True], repeat=3):

        sentence1 = implies(Q, P)
        sentence2 = implies(P, not Q)
        sentence3 = Q or R

        KB = sentence1 and sentence2 and sentence3

        print(
            int(P), int(Q), int(R), "|",
            int(sentence1), "   |",
            int(sentence2), "    |",
            int(sentence3), "  |",
            int(KB)
        )

        if KB:
            models.append((P, Q, R))

    print("\nModels of KB:", models)

    # Check entailment
    queries = {
        "R": lambda P, Q, R: R,
        "R -> P": lambda P, Q, R: implies(R, P),
        "Q -> R": lambda P, Q, R: implies(Q, R)
    }

    for query, function in queries.items():

        result = all(function(P, Q, R) for P, Q, R in models)

        print("KB entails", query, ":", result)


truth_table()