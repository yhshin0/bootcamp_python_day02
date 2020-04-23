def ft_map(function_to_apply, list_of_inputs):
    result = []
    for elem in list_of_inputs:
        result.append(function_to_apply(elem))
    return result


if __name__ == '__main__':
    lst = ['abc', 'dd', 'sdfsdx']
    print(list(map(len, lst)))
    print(list(ft_map(len, lst)))
