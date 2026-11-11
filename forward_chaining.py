
# Forward Chaining in First Order Logic

# Step 1: Initial facts in Knowledge Base
facts = {
    ("American", "Robert"),
    ("Enemy", "A", "America"),
    ("Owns", "A", "T1"),
    ("Missile", "T1")
}

# Step 2: Forward Chaining Algorithm
def forward_chaining(facts):

    new_facts = True

    while new_facts:
        new_facts = False

        # Rule 1: Enemy -> Hostile
        for fact in list(facts):
            if fact[0] == "Enemy":
                x = fact[1]
                y = fact[2]

                if y == "America":
                    new_fact = ("Hostile", x)

                    if new_fact not in facts:
                        facts.add(new_fact)
                        new_facts = True
                        print("Derived:", new_fact)

        # Rule 2: Missile -> Weapon
        for fact in list(facts):
            if fact[0] == "Missile":
                x = fact[1]
                new_fact = ("Weapon", x)

                if new_fact not in facts:
                    facts.add(new_fact)
                    new_facts = True
                    print("Derived:", new_fact)

        # Rule 3: Missile and Owns -> Sells
        for fact in list(facts):
            if fact[0] == "Missile":
                x = fact[1]

                if ("Owns", "A", x) in facts:
                    new_fact = ("Sells", "Robert", x, "A")

                    if new_fact not in facts:
                        facts.add(new_fact)
                        new_facts = True
                        print("Derived:", new_fact)

        # Rule 4: American + Weapon + Sells + Hostile -> Criminal
        for fact in list(facts):
            if fact[0] == "Sells":
                p, q, r = fact[1], fact[2], fact[3]

                if (("American", p) in facts and
                    ("Weapon", q) in facts and
                    ("Hostile", r) in facts):

                    new_fact = ("Criminal", p)

                    if new_fact not in facts:
                        facts.add(new_fact)
                        new_facts = True
                        print("Derived:", new_fact)

    return facts


# Step 3: Execute Forward Chaining
result = forward_chaining(facts)

# Step 4: Check Goal
print("\nFinal Knowledge Base:")
for fact in sorted(result):
    print(fact)

if ("Criminal", "Robert") in result:
    print("\nGoal Proved: Robert is a Criminal")
else:
    print("\nGoal Not Proved")
