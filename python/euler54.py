import doctest
# Learn rules

# Suites: H D C S
# Cards:  2 3 4 5 6 7 8 9 10 J Q K A
cards = {c:i for i, c in enumerate('2 3 4 5 6 7 8 9 T J Q K A'.split())}
suites = {c:i for i, c in enumerate('H D C S'.split())}

def is_straight(hand):
    pass

def is_full_house(hand):
    """
    >>> is_full_house('2H 2D 4C 4D 4S'.split())
    True
    """
    count = {c:0 for c in cards.keys()}
    for card in hand:
        count[card[0]] += 1
    for c in count:
        if count[c] != 0 and count[c] != 2 and count[c] != 3:
            return False
    return True

def is_flush(hand):
    """
    >>> is_flush('3D 6D 7D TD QD'.split())
    True
    >>> is_flush('3D 6D 7D TH QD'.split())
    False
    """
    suite = hand[0][1]
    for c in hand:
        if suite != c[1]:
            return False
    return True


# royal flush
def is_royal(hand):
    """
    >>> is_royal('TS JS QS KS AS'.split())
    True
    >>> is_royal('TH JS QS KS AS'.split())
    False
    """

    # same suit
    suite = hand[0][1]
    count = {c:0 for c in cards.keys()}
    for c in hand:
        if suite != c[1]:
            return False
        count[c[0]] += 1
    # all in same suit
    for c in 'T J Q K A'.split():
        if count[c] != 1:
            return False
    return True

def poker(p1, p2):
    return True

if __name__ == '__main__':
    doctest.testmod()
    p1_wins = 0
    with open('../data/p054_poker.txt') as f:
        for l in f.readlines():
            c = l.strip().split()
            p1 = c[:5]
            p2 = c[5:]
            # print('P1: {} P2: {}'.format(p1, p2))
            p1_wins += poker(p1, p2)
    print('{} wins'.format(p1_wins))
