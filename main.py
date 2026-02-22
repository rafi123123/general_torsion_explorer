from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup, simplify_presentation

# 1. Define the Free Group with generators x and y
F, x, y = free_group("x, y")

# 2. Define the relations for a Trefoil Knot: x^2 = y^3 
# In SymPy, relations are written as expressions equal to the identity (e)
# So x^2 * y^-3 = e
relations = [x**2 * y**-3]

# 3. Create the Finitely Presented Group
trefoil_group = FpGroup(F, relations)

# 4. Define a complex "word" that should reduce to identity
# For example: (x^2) * (y^-3) is identity by definition
word = x**2 * y**-3 * x**2 * y**-3

# 5. Simplify the word
reduced_word = trefoil_group.reduce(word)

print(f"Original expression: {word}")
print(f"Reduced expression: {reduced_word}")