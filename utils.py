from itertools import product


def get_n_letter_permutations(n: int):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
    for p in product(alphabet, repeat=n):
        yield ''.join(p)
