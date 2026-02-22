from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup, simplify_presentation

def create_indexed_fp_group(
        num_generators: int, 
        relation_strings:list[str] | None = None
    ):
    """
    Creates an FpGroup with generators named x_0, x_1, ... x_{n-1}.
    if no relation_strings are given then the free group is generated
    """
    # 1. Create indexed names: "x_0, x_1, x_2..."
    names = [f"x_{i}" for i in range(num_generators)]
    names_str = ", ".join(names)
    
    # 2. Initialize the Free Group
    F, *gens = free_group(names_str)
    
    # 3. Create a mapping for string evaluation
    # This maps the string "x_0" to the actual SymPy object x_0
    gen_dict = {name: gen for name, gen in zip(names, gens)}
    
    # 4. Parse the strings into SymPy expressions
    parsed_relations = []
    if relation_strings:
        for rel in relation_strings:
            # We allow the use of * for multiplication and ** for powers
            parsed_relations.append(eval(rel, {"__builtins__": None}, gen_dict))
    
    return FpGroup(F, parsed_relations)

