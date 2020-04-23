def ft_filter(function_to_apply, list_of_inputs):
    result = []
    for elem in list_of_inputs:
        if function_to_apply(elem):
            result.append(elem)
    return result


def test_is_string(arg):
    if isinstance(arg, str):
        return True
    return False


if __name__ == '__main__':
    lst = ['abc', 123, 'bzxc123']
    print(list(filter(test_is_string, lst)))
    print(list(ft_filter(test_is_string, lst)))
