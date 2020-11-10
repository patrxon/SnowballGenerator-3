import tuple_operations as tp

dirs = [(1, 1), (1, 0), (1, -1), (0, -1),
        (-1, -1), (-1, 0), (-1, 1), (0, 1)]

moves = ['r', 'l', 'j']


def split_sequence(string):
    sequences = []

    try:
        for seq in string.split('/'):
            temp = []
            temp += [(int(seq[0:2]), int(seq[2:4]))]
            temp += [tp.add_up((int(seq[0:2]), int(seq[2:4])), dirs[int(seq[4])])]
            pattern = [(seq[5])]
            num = ''

            for symbol in seq[6:]:
                if symbol in moves:
                    for i in range(int(num) - 1):
                        pattern += pattern[-1]
                    num = ''
                    pattern += [symbol]
                else:
                    num += symbol

            for i in range(int(num) - 1):
                pattern += pattern[-1]

            temp += [pattern]
            sequences += [temp]
    except:
        print("wrong pattern")

    return sequences
