import warnings
warnings.filterwarnings("ignore", message="Plink failed to import tkinter")

import snappy
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


def get_knot_data(limit=500):
    #FIXME
    knot_list = []
    # CensusKnots contains prime knots from the Rolfsen and HT tables
    for k in snappy.CensusKnots[1:limit]:
        # Get the fundamental group
        G = k.fundamental_group()
        
        # SnapPy naming is usually 'a, b, c...'
        # We can map these to your x_0, x_1... format
        num_gens = G.num_generators()
        relations = []
        
        for rel in G.relators():
            # SnapPy relators are strings like 'abCB' (Capital = inverse)
            # We convert these to your x_0 * x_1**-1 format
            # print('--------------------')
            # print(rel)
            # print('--------------------')
            formatted_rel = format_snappy_rel(rel, num_gens)
            relations.append(formatted_rel)
            
        knot_list.append({
            "name": k.name(),
            "generators": num_gens,
            "relations": relations
        })
    return knot_list

def format_snappy_rel(rel_str, num_gens):
    #FIXME
    # Mapping 'a'->x_0, 'b'->x_1, 'A'->x_0**-1, etc.
    components = []
    for char in rel_str:
        idx = ord(char.lower()) - ord('a')
        if char.isupper():
            components.append(f"x_{idx}**-1")
        else:
            components.append(f"x_{idx}")
    return " * ".join(components)

# if __name__ == '__main__':
    # Usage
    # j = 4
    # data = get_knot_data(j)
    # for entry in data:
    #     print(entry)
    # print(f"Retrieved {len(data)} knots.")
    # for entry in data:
    #     if len(entry['relations']) > 1:
    #         print(entry)
    #     # if entry['generators'] > 2:
    #     #     print(entry)