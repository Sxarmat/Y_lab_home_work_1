from operator import mul
from functools import reduce
from itertools import combinations_with_replacement


def count_find_num(primesL, limit):
    result_list = set()
    k = len(primesL)
    flag = True
    while flag is True:
        products = (reduce(mul, i) for i in combinations_with_replacement(primesL, k) if
                    not set(primesL).difference(set(i)))
        products_in_limit = set(filter(lambda x: x <= limit, products))
        if products_in_limit:
            result_list.update(products_in_limit)
            k += 1
        else:
            flag = False
    return [len(result_list), max(result_list)] if result_list else list()

