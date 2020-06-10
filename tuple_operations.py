def flip(tuple_):
    return tuple_[0], -tuple_[1]


def add_up(tuple_a, tuple_b):
    return tuple(map(sum, zip(tuple_a, tuple_b)))


def multiple(tuple_, size):
    return tuple([size * x for x in tuple_])


def calculate_pos(tuple_a, tuple_b, size):
    return add_up(tuple_a, multiple(flip(tuple_b), size))