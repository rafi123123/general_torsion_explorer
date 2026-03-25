# best conjugate multiple words for the 6_2 knot after 1 million random permutations

```
-----------------maximal exponent diff--------------
CsvData(knot_name_or_index='6_2',
        conjugate_multiple=x_1**-2*x_0**-1*x_1**-1*x_0**2*x_1**-1*x_0**-1*x_1*x_0**2*x_1**3*x_0**-1*x_1**-1*x_0*x_1**-1*x_0**2*x_1**-1*x_0**-1*x_1**2*x_0*x_1**-1*x_0**2*x_1**-2*x_0*x_1**-1*x_0**2*x_1**-1*x_0**-1*x_1**6*x_0**2*x_1**-1*x_0**-1*x_1*x_0*x_1**-4*x_0**-2*x_1**-2*x_0*x_1**-1*x_0**2*x_1**-1*x_0**-1*x_1**3*x_0**-2*x_1**3*x_0**-1*x_1**-1*x_0**2*x_1**-1*x_0**2*x_1**-1*x_0**-1*x_1*x_0**-1*x_1*x_0*x_1**-3*x_0**2*x_1**-3*x_0*x_1**-2*x_0*x_1*x_0**2*x_1**-1*x_0**-1*x_1*x_0*x_1**-2*x_0**-1*x_1**2*x_0**-1*x_1**3*x_0**-1*x_1*x_0*x_1**2*x_0*x_1**-1*x_0**2*x_1**-1*x_0**-1*x_1**-1*x_0**-1*x_1**-1*x_0*x_1**-1*x_0**2*x_1*x_0**2*x_1**-1*x_0**-1*x_1*x_0*x_1**-2*x_0**-2*x_1,
        torsion_element=x_1**-1*x_0**2*x_1**-1*x_0**-1*x_1*x_0,
        words=[   x_1**-2*x_0**-1,
                  x_1*x_0**-1*x_1**-1*x_0,
                  x_0**2*x_1**-2*x_0,
                  x_0**2*x_1**4,
                  x_1**-2*x_0,
                  x_0**-2*x_1**3*x_0**-1*x_1**-1*x_0**2,
                  x_1**-3*x_0*x_1**-2*x_0*x_1**2,
                  x_0**-1*x_1*x_0*x_1**2*x_0,
                  x_1**-1*x_0**2*x_1**2],
        exponent_summation_pre_reduction=141,
        exponent_summation_post_reduction=112,
        exponenet_diff_reduction=29,
        torsion_length=9,
        amount_of_words=9,
        max_torsion_element_length=10,
        min_torsion_element_length=2,
        max_word_length=15,
        min_word_length=0,
        max_amount_of_words=10,
        min_amount_of_words=2)
-------------------------------------------
```

**Maximal exponent reduction ratio**
```
knot_name_or_index                                                                                       6_2
conjugate_multiple                   x_1**2*x_0**-2*x_1**3*x_0**-1*x_1**-1*x_0**2*x_1**-3*x_0**2*x_1**-3*x_0
torsion_element                                                                                  x_1**-1*x_0
words                                                            [x_1**2*x_0**-2*x_1**3*x_0**-1, <identity>]
exponent_summation_pre_reduction                                                                          20
exponent_summation_post_reduction                                                                          5
exponenet_diff_reduction                                                                                  15
torsion_length                                                                                             4
amount_of_words                                                                                            2
max_torsion_element_length                                                                                10
min_torsion_element_length                                                                                 2
max_word_length                                                                                           15
min_word_length                                                                                            0
max_amount_of_words                                                                                       10
min_amount_of_words                                                                                        2
percent_reduced                                                                                         0.75
Name: 668168, dtype: object
```

```
In [21]: knot.fpgroup.reduce(create_conjugate_multiplication((x_1**-1*x_0), [(x_1**3*x_0**-2*x_1**3*
       ⋮ x_0**-1)]))
Out[21]: x_0*x_1**-2
```



```
-----------------maximal_exponent_percent_reduced--------------
CsvData(knot_name_or_index='6_2',
        conjugate_multiple=x_0**2*x_1**-3*x_0**2*x_1**-1*x_0**-1*x_1**3*x_0**-2*x_1**2*x_0**-1,
        reduced_conjugate_multiple=x_1*x_0*x_1**-1*x_0**-1,
        torsion_element=x_1**-1*x_0,
        words=[x_0**2*x_1**-3*x_0*x_1],
        exponent_summation_pre_reduction=17,
        exponent_summation_post_reduction=4,
        exponenet_diff_reduction=13,
        torsion_length=5,
        amount_of_words=1,
        percent_reduced=0.7647058823529411,
        max_torsion_element_length=10,
        min_torsion_element_length=2,
        max_word_length=15,
        min_word_length=0,
        fixed_word_length=None,
        max_amount_of_words=10,
        min_amount_of_words=2,
        right_multiple=x_1**2*x_0**-1,
        x_0_exponent_sum_no_abs_torsion_element=1,
        x_1_exponent_sum_no_abs_torsion_element=-1,
        x_2_exponent_sum_no_abs_torsion_element=None,
        x_3_exponent_sum_no_abs_torsion_element=None,
        x_0_exponent_sum_no_abs_conjigate_multiple_pre_reduction=0,
        x_1_exponent_sum_no_abs_conjigate_multiple_pre_reduction=1,
        x_2_exponent_sum_no_abs_conjigate_multiple_pre_reduction=None,
        x_3_exponent_sum_no_abs_conjigate_multiple_pre_reduction=None,
        x_0_exponent_sum_no_abs_conjigate_multiple_post_reduction=0,
        x_1_exponent_sum_no_abs_conjigate_multiple_post_reduction=0,
        x_2_exponent_sum_no_abs_conjigate_multiple_post_reduction=None,
        x_3_exponent_sum_no_abs_conjigate_multiple_post_reduction=None)
-------------------------------------------
```

```
-----------------maximal_exponent_percent_reduced--------------
CsvData(knot_name_or_index='6_2',
        conjugate_multiple=x_1**-1*x_0*x_1**-3*x_0**2*x_1**-3*x_0**2*x_1**-1*x_0**-1*x_1**3*x_0**-2*x_1**3*x_0**-1*x_1*x_0*x_1**-2,
        reduced_conjugate_multiple=x_1**-1*x_0*x_1**-1*x_0*x_1**-2,
        torsion_element=x_1**-1*x_0,
        words=[x_1**-1*x_0*x_1**-3*x_0**2*x_1**-3*x_0**2],
        exponent_summation_pre_reduction=27,
        exponent_summation_post_reduction=6,
        exponenet_diff_reduction=21,
        torsion_length=6,
        amount_of_words=1,
        percent_reduced=0.7777777777777778,
        max_torsion_element_length=10,
        min_torsion_element_length=2,
        max_word_length=15,
        min_word_length=0,
        fixed_word_length=None,
        max_amount_of_words=10,
        min_amount_of_words=2,
        right_multiple=x_0*x_1**-2,
        x_0_exponent_sum_no_abs_torsion_element=1,
        x_1_exponent_sum_no_abs_torsion_element=-1,
        x_2_exponent_sum_no_abs_torsion_element=None,
        x_3_exponent_sum_no_abs_torsion_element=None,
        x_0_exponent_sum_no_abs_conjigate_multiple_pre_reduction=2,
        x_1_exponent_sum_no_abs_conjigate_multiple_pre_reduction=-3,
        x_2_exponent_sum_no_abs_conjigate_multiple_pre_reduction=None,
        x_3_exponent_sum_no_abs_conjigate_multiple_pre_reduction=None,
        x_0_exponent_sum_no_abs_conjigate_multiple_post_reduction=2,
        x_1_exponent_sum_no_abs_conjigate_multiple_post_reduction=-4,
        x_2_exponent_sum_no_abs_conjigate_multiple_post_reduction=None,
        x_3_exponent_sum_no_abs_conjigate_multiple_post_reduction=None)
-------------------------------------------
```

```
-----------------maximal_exponent_percent_reduced--------------
CsvData(knot_name_or_index='6_2',
        conjugate_multiple=x_0**-1*x_1**3*x_0**-2*x_1**3*x_0**-1*x_1**-1*x_0**2*x_1**-3*x_0**2*x_1**-3*x_0**2*x_1**-2,
        reduced_conjugate_multiple=x_1**-2*x_0**2*x_1**-2,
        torsion_element=x_1**-1*x_0,
        words=[x_0**-1*x_1**3*x_0**-2*x_1**3*x_0**-1],
        exponent_summation_pre_reduction=25,
        exponent_summation_post_reduction=6,
        exponenet_diff_reduction=19,
        torsion_length=5,
        amount_of_words=1,
        percent_reduced=0.76,
        max_torsion_element_length=10,
        min_torsion_element_length=2,
        max_word_length=15,
        min_word_length=0,
        fixed_word_length=None,
        max_amount_of_words=10,
        min_amount_of_words=2,
        right_multiple=x_0*x_1**-2,
        x_0_exponent_sum_no_abs_torsion_element=1,
        x_1_exponent_sum_no_abs_torsion_element=-1,
        x_2_exponent_sum_no_abs_torsion_element=None,
        x_3_exponent_sum_no_abs_torsion_element=None,
        x_0_exponent_sum_no_abs_conjigate_multiple_pre_reduction=2,
        x_1_exponent_sum_no_abs_conjigate_multiple_pre_reduction=-3,
        x_2_exponent_sum_no_abs_conjigate_multiple_pre_reduction=None,
        x_3_exponent_sum_no_abs_conjigate_multiple_pre_reduction=None,
        x_0_exponent_sum_no_abs_conjigate_multiple_post_reduction=2,
        x_1_exponent_sum_no_abs_conjigate_multiple_post_reduction=-4,
        x_2_exponent_sum_no_abs_conjigate_multiple_post_reduction=None,
        x_3_exponent_sum_no_abs_conjigate_multiple_post_reduction=None)
-------------------------------------------
```