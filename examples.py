from main import (
    create_indexed_fp_group, 
    get_knot_data, 
    sum_absolute_exponents,
    create_conjugate_multiplication,
    sum_per_generator_exponent
)

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
    knot = get_knot_data(0)
    print(knot.relations)
    print(knot.fpgroup.relators)


def test_sum_absolute_exponents():
    """
    Test the sum_absolute_exponents function with various word examples.
    """
    print("Testing sum_absolute_exponents function:")
    print("-" * 50)
    
    # Create an indexed FP group with 3 generators
    fp_group = create_indexed_fp_group(3)
    
    # Extract generators from the group
    F = fp_group.free_group
    x0, x1, x2 = F.generators
    
    # Test case 1: Simple word with positive exponents
    word1 = x0 * x1 * x2
    result1 = sum_absolute_exponents(word1)
    print(f"Word: {word1}")
    print(f"Sum of absolute exponents: {result1}")
    print(f"Expected: 3 (|1| + |1| + |1|)")
    print()
    
    # Test case 2: Word with negative exponents
    word2 = x0 * x1**(-2) * x0**3
    result2 = sum_absolute_exponents(word2)
    print(f"Word: {word2}")
    print(f"Sum of absolute exponents: {result2}")
    print(f"Expected: 6 (|1| + |-2| + |3|)")
    print()
    
    # Test case 3: Word with larger exponents
    word3 = x0**(-4) * x2**5 * x1**(-1)
    result3 = sum_absolute_exponents(word3)
    print(f"Word: {word3}")
    print(f"Sum of absolute exponents: {result3}")
    print(f"Expected: 10 (|-4| + |5| + |-1|)")
    print()
    
    # Test case 4: Single generator with high exponent
    word4 = x1**7
    result4 = sum_absolute_exponents(word4)
    print(f"Word: {word4}")
    print(f"Sum of absolute exponents: {result4}")
    print(f"Expected: 7 (|7|)")


def test_conjigate_maker():
    knot = get_knot_data(0).fpgroup
    x_0, x_1 = knot.generators
    print(create_conjugate_multiplication(x_0, [x_1]))
    print(create_conjugate_multiplication(x_0, [x_1, x_0**2*x_1]))


def test_get_exponent_per_generator():
    free_group = create_indexed_fp_group(4)
    x_0, x_1, x_2, x_3 = free_group.generators
    word = (x_0**3 * x_3**5)
    print(sum_per_generator_exponent(word))

if __name__ == '__main__':
    # print('-----trefoil_example()------')
    # trefoil_example()
    # print('-----free_group()------')
    # free_group()
    # print('------figure_eight_example()-----')
    # figure_eight_example()
    # print('----knuth_bendix_reduction_algorithm()-------')
    # knuth_bendix_reduction_algorithm()
    # print('------using_snappy_knot_data()-----')
    # using_snappy_knot_data()
    # print('-----------')
    # print('------test_sum_absolute_exponents()-----')
    # test_sum_absolute_exponents()
    # print('-----------')
    # print('------test_conjigate_maker()-----')
    # test_conjigate_maker()
    # print('-----------')
    print('------test_get_exponent_per_generator()-----')
    test_get_exponent_per_generator()
    print('-----------')
    
