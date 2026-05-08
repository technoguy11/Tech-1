# Practical 3 - Clean Output Version (Fixed Precision)

# Function to round list values
def round_list(lst, digits=2):
    return [round(x, digits) for x in lst]


# Define fuzzy sets
A = [0, 1, 0.7, 0.4, 0.2]
B = [0, 0.4, 0.7, 0.8, 1]

print("Fuzzy Set A:", A)
print("Fuzzy Set B:", B)


# -------------------------
# UNION
# -------------------------
union = round_list([max(a, b) for a, b in zip(A, B)])
print("\nUnion (A ∪ B):", union)


# -------------------------
# INTERSECTION
# -------------------------
intersection = round_list([min(a, b) for a, b in zip(A, B)])
print("Intersection (A ∩ B):", intersection)


# -------------------------
# COMPLEMENT
# -------------------------
complement_A = round_list([1 - a for a in A])
print("Complement of A:", complement_A)


# -------------------------
# DIFFERENCE
# -------------------------
difference = round_list([min(a, 1 - b) for a, b in zip(A, B)])
print("Difference (A - B):", difference)


# -------------------------
# CARTESIAN PRODUCT
# -------------------------
relation = []
for a in A:
    row = []
    for b in B:
        row.append(round(min(a, b), 2))
    relation.append(row)

print("\nFuzzy Relation (Cartesian Product):")
for row in relation:
    print(row)


# -------------------------
# MAX-MIN COMPOSITION
# -------------------------
X = [0.9, 0.4, 0.0]

R = [
    [0.5, 1, 0.3],
    [0.5, 0.8, 0.3],
    [0.0, 0.6, 0.3]
]

result = []

for j in range(len(R[0])):
    values = []
    for i in range(len(X)):
        values.append(min(X[i], R[i][j]))
    result.append(round(max(values), 2))

print("\nMax-Min Composition Result:", result)