import itertools


def bananas(str_in):
    pattern = 'banana'
    result = set()
    for index_combination in itertools.combinations(range(len(str_in)), len(str_in) - len(pattern)):
        str_in_list = list(str_in)
        for index in index_combination:
            str_in_list[index] = '-'
        combination = ''.join(str_in_list)
        if combination.replace('-', '') == pattern:
            result.add(combination)
    return result
