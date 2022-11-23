from string import ascii_lowercase as alpha


def alphabet_position(text):
    return ' '.join(str(alpha.index(letter) + 1) for letter in text.lower() if letter in alpha)
