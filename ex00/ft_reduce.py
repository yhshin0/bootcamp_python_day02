def ft_reduce(function_to_apply, list_of_inputs):
    it = iter(list_of_inputs)
    result = next(it)
    for elem in it:
        result = function_to_apply(result, elem)
    return result


def test_add(a, b):
    return a + b


from functools import reduce

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    print(reduce(test_add, lst))
    print(ft_reduce(test_add, lst))
