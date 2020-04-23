def what_are_the_vars(*args, **kwargs):
    """Your code"""
    obj = ObjectC()
    for idx in range(len(args)):
        key = 'var_' + str(idx)
        obj.__setattr__(key, args[idx])
    for k, v in kwargs.items():
        try:
            if obj.__getattribute__(k) is not None:
                return None
        except AttributeError:
            pass
        obj.__setattr__(k, v)
    return obj


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
