import doctest
# Learn rules

# Suites: H D C S
# Cards:  2 3 4 5 6 7 8 9 10 J Q K A
cards = {c:i for i, c in enumerate('23456789TJQKA', start=2)}
suites = {c:i for i, c in enumerate('HDCS', start=1)}

def is_contiguous(arr):
    """ return True if values of array are consecutive integers
    >>> is_contiguous([2, 5, 3, 4])
    True
    >>> is_contiguous([9, 5, 8, 7, 6])
    True
    >>> is_contiguous([1, 5, 3, 4])
    False
    >>> is_contiguous([1, 2, 3, 0])
    True
    """
    mn, mx = min(arr), max(arr)
    s = sum(arr)
    sn = (mn*(mn-1))/2 if mn!=0 else 0
    sx = (mx*(mx+1))/2
    if s == sx-sn:
        return True
    else:
        return False

def is_straight(hand):
    """ All cards are consecutive values of the same suite
    >>> is_straight('9H TH JH KH QH'.split())
    True
    >>> is_straight('9H TD JH KH QH'.split())
    False
    """
    # same suite
    suite = hand[0][1]
    vals = []
    for c in hand:
        if suite !=  c[1]:
            return False
        vals.append(cards[c[0]])
    # check if vals are consecutive or not
    if is_contiguous(vals):
        return True
    else:
        return False


def is_full_house(hand):
    """ Three of a kind and a pair
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
    """ All cards of the same suite
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


def is_four_of_a_kind(hand):
    """ four cards of the same value
    >>> is_four_of_a_kind('2H 2D 2C 2S 4H'.split())
    (True, 0)
    >>> is_four_of_a_kind('2H 2D 2C 3S 4H'.split())
    """
    count = {c:0 for c in cards.keys()}
    for card in hand:
        count[card[0]] += 1
    for c in count:
        if count[c] == 4:
            return (True, cards[c])
    return None

# royal flush
def is_royal(hand):
    """ Ten Jack Queen King Ace, from the same suite
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
    if is_royal(p1):
        return True
    return False

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
