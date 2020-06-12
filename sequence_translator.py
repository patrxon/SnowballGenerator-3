

def translate_sequence(sequence):
    translated = []

    for move in sequence:
        for i in range(sequence[move]):
            translated.append(move)

    return translated