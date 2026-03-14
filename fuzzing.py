import csv
import random
from main import (
    get_knot_data, 
    sum_absolute_exponents,
    create_conjugate_multiplication
)
from pathlib import Path
import os
from dataclasses import dataclass, asdict
from datetime import datetime
from pprint import pprint
import atexit

@dataclass
class CsvData:
    knot_name_or_index: str | int | None = None
    conjugate_multiple: str | None = None
    torsion_element: str | None = None
    words: str | None = None
    exponent_summation_pre_reduction: int | None = None
    exponent_summation_post_reduction: int | None = None
    exponenet_diff_reduction: int | None = None
    torsion_length: int | None = None
    amount_of_words: int | None = None
    max_torsion_element_length: int | None = None
    min_torsion_element_length: int | None = None
    max_word_length: int | None = None
    min_word_length: int | None = None
    max_amount_of_words: int | None = None
    min_amount_of_words: int | None = None



def knot_torsion_random_fuzzer(
        knot_name_or_index : str | int,
        output_filename: str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S"),
        fuzzing_limit: int = 1_0,
        max_torsion_element_length: int = 10,
        min_torsion_element_length: int = 2,
        max_word_length: int = 15,
        min_word_length: int = 0,
        max_amount_of_words: int = 10,
        min_amount_of_words: int = 2,

    ) -> None:

    maximal_exponent_sum_diff = CsvData(exponenet_diff_reduction=-1)
    
    def cleanup():
        print(f"-----------------maximal exponent diff--------------")
        pprint(maximal_exponent_sum_diff,indent=4)
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

        generators: tuple = knot.fpgroup.generators
        generators_with_inverses = list(generators) + [gen**-1 for gen in generators]
        identity = knot.fpgroup.identity

        for _ in range(fuzzing_limit):
            csv_data = CsvData()
            csv_data.knot_name_or_index = knot_name_or_index
            csv_data.max_torsion_element_length = max_torsion_element_length
            csv_data.min_torsion_element_length = min_torsion_element_length
            csv_data.max_word_length = max_word_length
            csv_data.min_word_length = min_word_length
            csv_data.max_amount_of_words = max_amount_of_words
            csv_data.min_amount_of_words = min_amount_of_words
            csv_data.torsion_length = random.randint(min_torsion_element_length, max_torsion_element_length)

            torsion = identity

            while torsion == identity: # making sure the torsion element is not trivial
                torsion_elements = random.choices(generators_with_inverses, k=csv_data.torsion_length)
                torsion = identity
                for elem in torsion_elements:
                    torsion = torsion*elem
                torsion = knot.fpgroup.reduce(torsion)
            csv_data.torsion_element = torsion

            csv_data.amount_of_words = random.randint(min_amount_of_words, max_amount_of_words)
            words = []
            for _ in range(csv_data.amount_of_words):
                word_length = random.randint(min_word_length, max_word_length)
                word_elements = random.choices(generators_with_inverses, k=word_length)
                word = identity
                for elem in word_elements:
                    word = word*elem
                words.append(word)
            csv_data.words = words
            csv_data.conjugate_multiple = create_conjugate_multiplication(torsion, words)
            csv_data.exponent_summation_pre_reduction = sum_absolute_exponents(csv_data.conjugate_multiple)
            csv_data.exponent_summation_post_reduction = sum_absolute_exponents(
                    knot.fpgroup.reduce(csv_data.conjugate_multiple)
                )
            csv_data.exponenet_diff_reduction = \
                csv_data.exponent_summation_pre_reduction - csv_data.exponent_summation_post_reduction
            if csv_data.exponenet_diff_reduction > maximal_exponent_sum_diff.exponenet_diff_reduction:
                maximal_exponent_sum_diff = csv_data

            writer.writerow(asdict(csv_data))
            


        
        
if __name__ == '__main__':
    knot_torsion_random_fuzzer('6_2', output_filename='initial', fuzzing_limit=10000)
