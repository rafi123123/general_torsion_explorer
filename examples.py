from main import create_indexed_fp_group, get_knot_data

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
    """
    there exists a way to collapse this group to
    only two generators and one relationship.
    """
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
    print(figure_eight.reduce(word))

def knuth_bendix_reduction_algorithm():
    """
    the Knuth-Bendix recution algorithm is the algorithm 
    that applies the reduction rules to a word attempting to make it as small as possible
    this should be done by the .reduce() method. here i am checking that
    """

    test_rel = "x_0*x_1*x_2**4" 
    test_knot = create_indexed_fp_group(3, [test_rel])
    x_0, x_1, x_2 = test_knot.generators
    word = x_1*x_2**3
    print(test_knot.reduce(word))

def using_snappy_knot_data():
    knot_data = get_knot_data(0)
    print(knot_data.relations)
    knot = create_indexed_fp_group(knot_data.num_gens, knot_data.relations)
    print(knot.relators)


if __name__ == '__main__':
    # print('-----trefoil_example()------')
    # trefoil_example()
    # print('-----free_group()------')
    # free_group()
    # print('------figure_eight_example()-----')
    # figure_eight_example()
    # print('----knuth_bendix_reduction_algorithm()-------')
    # knuth_bendix_reduction_algorithm()
    print('------using_snappy_knot_data()-----')
    using_snappy_knot_data()
    print('-----------')
