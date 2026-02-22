from main import create_indexed_fp_group

def free_group():
    free_group = create_indexed_fp_group(4)
    x_0, x_1, x_2, x_3 = free_group.generators
    word = (x_0**3 * x_3**5)**-2
    print(free_group.reduce(word))

def trefoil_example():
    trefoil_rel = "x_0**2 * x_1**-3" # the expression that should evaluate to the identity
    trefoil = create_indexed_fp_group(2, [trefoil_rel])
    x_0, x_1 = trefoil.generators
    
    rel_identity = x_0**2 *x_1**-3
    word_to_identity =  (x_0**-2 * x_1**-1 * x_0 * x_1 * x_0 * x_0**-1 * x_1**-1 * x_0 * x_1)
    print(trefoil.reduce(word_to_identity) == trefoil.identity) # True
    print(trefoil.reduce(rel_identity) == trefoil.identity) # True

def figure_eight_example():
    fig8_relations = [
        "x_0 * x_2 * x_0**-1 * x_1**-1",
        "x_3 * x_1 * x_3**-1 * x_2**-1",
        "x_2 * x_0 * x_2**-1 * x_3**-1"
    ] # all the figure eight knot relationships
    figure_eight = create_indexed_fp_group(4, fig8_relations)
    x_0, x_1, x_2, x_3 = figure_eight.generators

    identity_words = [
        x_0 * x_2 * x_0**-1 * x_1**-1,
        x_3 * x_1 * x_3**-1 * x_2**-1,
        x_2 * x_0 * x_2**-1 * x_3**-1
    ]

    for word in identity_words:
        print(figure_eight.reduce(word) == figure_eight.identity) # True
    
    word = x_0**2 * (x_2 * x_0 * x_2**-1 * x_3**-1) * (x_2 * x_0**-1 * x_1**-1)
    snappy_words = [
        'x_0 * x_0 * x_1 * x_1 * x_0**-1 * x_1**-1 * x_1**-1'
    ]
    print(figure_eight.reduce(word))


def using_snappy_example():
    """
    TODO
    """
    ...


if __name__ == '__main__':
    print('-----------')
    trefoil_example()
    print('-----------')
    free_group()
    print('-----------')
    figure_eight_example()
    print('-----------')
