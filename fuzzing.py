import csv
import random
from main import (
    get_knot_data, 
    sum_absolute_exponents,
    create_conjugate_multiplication,
    sum_per_generator_exponent
)
from pathlib import Path
import os
from dataclasses import dataclass, asdict
from datetime import datetime
from pprint import pprint
import atexit
from sympy.combinatorics.free_groups import FreeGroupElement

@dataclass
class CsvData:
    knot_name_or_index: str | int | None = None
    conjugate_multiple: str | None = None
    reduced_conjugate_multiple: str | None = None
    torsion_element: str | None = None
    words: str | None = None
    exponent_summation_pre_reduction: int | None = None
    exponent_summation_post_reduction: int | None = None
    exponenet_diff_reduction: int | None = None
    torsion_length: int | None = None
    amount_of_words: int | None = None
    percent_reduced: float | None = None
    max_torsion_element_length: int | None = None
    min_torsion_element_length: int | None = None
    max_word_length: int | None = None
    min_word_length: int | None = None
    fixed_word_length: int | None = None
    max_amount_of_words: int | None = None
    min_amount_of_words: int | None = None
    amount_of_words: int | None = None
    right_multiple: str | FreeGroupElement | None = None,

    x_0_exponent_sum_no_abs_torsion_element: int | None = None
    x_1_exponent_sum_no_abs_torsion_element: int | None = None
    x_2_exponent_sum_no_abs_torsion_element: int | None = None
    x_3_exponent_sum_no_abs_torsion_element: int | None = None
    
    x_0_exponent_sum_no_abs_conjigate_multiple_pre_reduction: int | None = None
    x_1_exponent_sum_no_abs_conjigate_multiple_pre_reduction: int | None = None
    x_2_exponent_sum_no_abs_conjigate_multiple_pre_reduction: int | None = None
    x_3_exponent_sum_no_abs_conjigate_multiple_pre_reduction: int | None = None
    
    x_0_exponent_sum_no_abs_conjigate_multiple_post_reduction: int | None = None
    x_1_exponent_sum_no_abs_conjigate_multiple_post_reduction: int | None = None
    x_2_exponent_sum_no_abs_conjigate_multiple_post_reduction: int | None = None
    x_3_exponent_sum_no_abs_conjigate_multiple_post_reduction: int | None = None

def knot_torsion_random_fuzzer(
        knot_name_or_index : str | int,
        output_filename: str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S"),
        fuzzing_limit: int = 10,
        max_torsion_element_length: int = 10,
        min_torsion_element_length: int = 2,
        max_word_length: int = 15,
        min_word_length: int = 0,
        fixed_word_length: int | None = None,
        max_amount_of_words: int | None = 10,
        min_amount_of_words: int | None = 2,
        amount_of_words: int | None = None,
        torsion_length: int | None = None,
        torsion_element: str | FreeGroupElement | None = None,
        right_multiple: str | FreeGroupElement | None = None,

    ) -> None:

    maximal_exponent_percent_reduced = CsvData(percent_reduced=-1)
    
    def cleanup():
        print(f"-----------------maximal_exponent_percent_reduced--------------")
        pprint(maximal_exponent_percent_reduced,indent=4)
        print('-------------------------------------------')
    atexit.register(cleanup)


    filename = Path(__file__).parent/'generated_data'/f'{knot_name_or_index}-{output_filename}.csv'
    file_exists = os.path.isfile(filename) and os.stat(filename).st_size > 0
    with open(filename, mode='a', newline='') as file:
        fieldnames = list(CsvData.__annotations__.keys())
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        
        knot = get_knot_data(knot_name_or_index)
        if knot.num_gens > 4:
            raise Warning(
                f"only 4 generator's exponents are accounted for. the knot group for {knot_name_or_index} has {knot.num_gens} generators"
            )

        generators: tuple = knot.fpgroup.generators
        generators_with_inverses = list(generators) + [gen**-1 for gen in generators]
        identity = knot.fpgroup.identity


        
        if torsion_element:
            if not isinstance(torsion_element, str):
                raise ValueError("manual torsion element must be strings that get evaluated. for example: \"x_1**-1*x_0\" (as a string)")
            _torsion_element = eval(
                torsion_element,
                {"__builtins__": None}, 
                {f'x_{i}': val for i, val in enumerate(generators)}
            )
        else:
            _torsion_element = None


        if right_multiple:
            if not isinstance(right_multiple, str):
                raise ValueError("manual right_multiple element must be strings that get evaluated. for example: \"x_1**-1*x_0\" (as a string)")
            _right_multiple = eval(
                right_multiple,
                {"__builtins__": None}, 
                {f'x_{i}': val for i, val in enumerate(generators)}
            )
        else:
            _right_multiple = identity




        for _ in range(fuzzing_limit):
            csv_data = CsvData(
                knot_name_or_index = knot_name_or_index,
                max_torsion_element_length = max_torsion_element_length,
                min_torsion_element_length = min_torsion_element_length,
                max_word_length = max_word_length,
                min_word_length = min_word_length,
                max_amount_of_words = max_amount_of_words,
                min_amount_of_words = min_amount_of_words,
                amount_of_words = amount_of_words or random.randint(min_amount_of_words, max_amount_of_words),
                torsion_length = torsion_length or random.randint(min_torsion_element_length, max_torsion_element_length),
                fixed_word_length=fixed_word_length,
                right_multiple=_right_multiple
            )
            
            if _torsion_element:
                csv_data.torsion_element = _torsion_element
            else:
                torsion = identity
                while torsion == identity: # making sure the torsion element is not trivial
                    torsion_elements = random.choices(generators_with_inverses, k=csv_data.torsion_length)
                    torsion = identity
                    for elem in torsion_elements:
                        torsion = torsion*elem
                    torsion = knot.fpgroup.reduce(torsion)
                csv_data.torsion_element = torsion

            words = []
            for _ in range(csv_data.amount_of_words):
                word_length = csv_data.fixed_word_length or random.randint(csv_data.min_word_length, csv_data.max_word_length)
                word_elements = random.choices(generators_with_inverses, k=word_length)
                word = identity
                for elem in word_elements:
                    word = word*elem
                words.append(word)
            csv_data.words = words
            csv_data.conjugate_multiple = create_conjugate_multiplication(csv_data.torsion_element, words) * csv_data.right_multiple
            csv_data.exponent_summation_pre_reduction = sum_absolute_exponents(csv_data.conjugate_multiple)
            csv_data.reduced_conjugate_multiple = knot.fpgroup.reduce(csv_data.conjugate_multiple)
            csv_data.exponent_summation_post_reduction = sum_absolute_exponents(
                    csv_data.reduced_conjugate_multiple
                )
            csv_data.exponenet_diff_reduction = \
                csv_data.exponent_summation_pre_reduction - csv_data.exponent_summation_post_reduction
            csv_data.percent_reduced = csv_data.exponenet_diff_reduction / csv_data.exponent_summation_pre_reduction
            

            for key, val in sum_per_generator_exponent(csv_data.torsion_element).items():
                setattr(csv_data, f"{key}_exponent_sum_no_abs_torsion_element", val)
            

            for key, val in sum_per_generator_exponent(csv_data.conjugate_multiple).items():
                setattr(csv_data, f"{key}_exponent_sum_no_abs_conjigate_multiple_pre_reduction", val)
            
            for key, val in sum_per_generator_exponent(csv_data.reduced_conjugate_multiple).items():
                setattr(csv_data, f"{key}_exponent_sum_no_abs_conjigate_multiple_post_reduction", val)


            if csv_data.percent_reduced > maximal_exponent_percent_reduced.percent_reduced:
                maximal_exponent_percent_reduced = csv_data

            writer.writerow(asdict(csv_data))
            
        
if __name__ == '__main__':
    knot_torsion_random_fuzzer(
        '6_2', 
        output_filename='large_test_x_1_-1_times_x_0', 
        torsion_element='x_1**-1*x_0', 
        right_multiple='x_0*x_1**-2',
        amount_of_words=1,
        fuzzing_limit=10_000_000
    )
