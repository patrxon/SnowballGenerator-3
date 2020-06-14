

def translate_sequence(sequence):
    translated = []

    for move in sequence:
        for i in range(move[1]):
            translated.append(move[0])

    return translated