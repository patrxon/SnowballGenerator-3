def flip(tuple_, first=False, second=False):
    if first:
        t1 = -tuple_[0]
    else:
        t1 = tuple_[0]
    if second:
        t2 = -tuple_[1]
    else:
        t2 = tuple_[1]
    return t1, t2


def add_up(tuple_a, tuple_b):
    return tuple(map(sum, zip(tuple_a, tuple_b)))


def subtract(tuple_a, tuple_b):
    return add_up(tuple_a, flip(tuple_b, True, True))


def multiple(tuple_, size):
    return tuple([size * x for x in tuple_])


def divide(tuple_, size):
    return tuple([int(x / size) for x in tuple_])


def calculate_pos(tuple_a, tuple_b, size):
    return add_up(tuple_a, multiple(flip(tuple_b, second=True), size))
