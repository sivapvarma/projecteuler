import doctest
# Learn rules

# Suites: H D C S
# Cards:  2 3 4 5 6 7 8 9 10 J Q K A
cards = {c:i for i, c in enumerate('23456789TJQKA', start=2)}
cards_keys = '23456789TJQKA'
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

def is_straight_flush(hand):
    """ All cards are consecutive values of the same suite
    >>> is_straight_flush('9H TH JH KH QH'.split())
    (True, 13)
    >>> is_straight_flush('9H TD JH KH QH'.split())
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
        return (True, max(vals))
    else:
        return False

def is_straight(hand):
    """ All cards are consecutive values
    >>> is_straight('9H TH JH KH QH'.split())
    True
    >>> is_straight('9H TD JH KH QH'.split())
    True
    """
    # same suite
    suite = hand[0][1]
    vals = []
    for c in hand:
        vals.append(cards[c[0]])
    # check if vals are consecutive or not
    if is_contiguous(vals):
        return True
    else:
        return False

def is_full_house(hand):
    """ Three of a kind and a pair
    >>> is_full_house('2H 2D 4C 4D 4S'.split())
    (True, 4)
    """
    count = {c:0 for c in cards.keys()}
    for card in hand:
        count[card[0]] += 1
    for c in count:
        if count[c] != 0 and count[c] != 2 and count[c] != 3:
            return None
    triple = 0
    for k in count:
        if count[k] == 3:
            triple = cards[k]
    return (True, triple)

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

def is_three_of_a_kind(hand):
    """ four cards of the same value
    >>> is_three_of_a_kind('2H 2D 2C 2S 4H'.split())
    >>> is_three_of_a_kind('2H 2D 2C 3S 4H'.split())
    (True, 2)
    """
    count = {c:0 for c in cards.keys()}
    for card in hand:
        count[card[0]] += 1
    for c in count:
        if count[c] == 3:
            return (True, cards[c])
    return None

def is_two_pairs(hand):
    count = {c:0 for c in cards.keys()}
    for card in hand:
        count[card[0]] += 1
    freq_count = {k:0 for k in range(6)}
    for k in count:
        freq_count[count[k]] += 1
    if freq_count[2] == 2:
        for k in reversed(cards_keys):
            if count[k]==2:
                return (True, cards[k])
    return None

def is_one_pair(hand):
    count = {c:0 for c in cards.keys()}
    for card in hand:
        count[card[0]] += 1
    freq_count = {k:0 for k in range(6)}
    for k in count:
        freq_count[count[k]] += 1
    if freq_count[2] == 1:
        for k in reversed(cards_keys):
            if count[k]==2:
                return (True, cards[k])
    return None

def highest_card(hand):
    vals = []
    for card in hand:
        vals.append(cards[card[0]])
    return max(vals)

def is_four_of_a_kind(hand):
    """ four cards of the same value
    >>> is_four_of_a_kind('2H 2D 2C 2S 4H'.split())
    (True, 2)
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
def is_royal_flush(hand):
    """ Ten Jack Queen King Ace, from the same suite
    >>> is_royal_flush('TS JS QS KS AS'.split())
    True
    >>> is_royal_flush('TH JS QS KS AS'.split())
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

    p1_wins = False

    # royal flush
    if is_royal_flush(p1) and not is_royal_flush(p2):
        # return True
        p1_wins = True
        # return p1_wins
        return (True, 10)
    if is_royal_flush(p2) and not is_royal_flush(p1):
        p1_wins = False
        return p1_wins
    if is_royal_flush(p1) and is_royal_flush(p2):
        if highest_card(p1) > highest_card(p2):
            return (True, 10)
        elif highest_card(p1) < highest_card(p2):
            return False

    # straight flush
    if is_straight_flush(p1) and not is_straight_flush(p2):
        p1_wins = True
        return (True, 9)
    if is_straight_flush(p2) and not is_straight_flush(p1):
        p1_wins = False
        return p1_wins
    if is_straight_flush(p1) and is_straight_flush(p2):
        p1_sf = is_straight_flush(p1)
        p2_sf = is_straight_flush(p2)
        if p1_sf[1] > p2_sf[1]:
            return (True, 9)
        elif p1_sf[1] < p2_sf[1]:
            return False

    # four of a kind
    p1_4 = is_four_of_a_kind(p1)
    p2_4 = is_four_of_a_kind(p2)
    if p1_4 and p2_4:
        if p1_4[1] > p2_4[1]:
            return (True, 8)
        else:
            return False
    elif p1_4:
        return (True, 8)
    elif p2_4:
        return False

    # full house
    p1_fh = is_full_house(p1)
    p2_fh = is_full_house(p2)
    if p1_fh and p2_fh:
        if p1_fh[1] > p2_fh[1]:
            return (True, 7)
        elif p1_fh[1] < p2_fh[1]:
            return False
    elif p1_fh:
        return (True, 7)
    elif p2_fh:
        return False

    # flush
    if is_flush(p1) and not is_flush(p2):
        return (True, 6)
    if is_flush(p2) and not is_flush(p1):
        return False
    if is_flush(p1) and is_flush(p2):
        if highest_card(p1) > highest_card(p2):
            return (True, 6)
        elif highest_card(p1) < highest_card(p2):
            return False

    # straight
    if is_straight(p1) and not is_straight(p2):
        p1_wins = (True, 5)
        return p1_wins
    if is_straight(p2) and not is_straight(p1):
        p1_wins = False
        return p1_wins

    # three of a kind
    p1_3 = is_three_of_a_kind(p1)
    p2_3 = is_three_of_a_kind(p2)
    if p1_3 and p2_3:
        if p1_3[1] > p2_3[1]:
            return (True, 4)
        elif p1_3[1] < p2_3[1]:
            return False
    elif p1_3:
        return (True, 4)
    elif p2_3:
        return False

    # two pairs
    p1_2 = is_two_pairs(p1)
    p2_2 = is_two_pairs(p2)
    if p1_2 and p2_2:
        if p1_2[1] > p2_2[1]:
            return (True, 3)
        elif p1_2[1] < p2_2[1]:
            return False
    elif p1_2:
        return (True, 3)
    elif p2_2:
        return False

    # pair
    p1_1p = is_one_pair(p1)
    p2_1p = is_one_pair(p2)
    if p1_1p and p2_1p:
        if p1_1p[1] > p2_1p[1]:
            return (True, 2)
        elif p1_1p[1] < p2_1p[1]:
            return False
    elif p1_1p:
        return (True, 2)
    elif p2_1p:
        return False

    # highest card
    # p1_wins = True
    if highest_card(p1) > highest_card(p2):
        return (True, 1)
    elif highest_card(p1) < highest_card(p2):
        return False
    return -1000

if __name__ == '__main__':
    doctest.testmod()
    p1_wins = 0
    with open('../data/p054_poker.txt') as f:
        for l in f.readlines():
            c = l.strip().split()
            p1 = c[:5]
            p2 = c[5:]
            if poker(p1, p2):
                print('P1: {} P2: {}'.format(p1, p2))
                p1_wins += 1 # poker(p1, p2)
    print('{} wins'.format(p1_wins))
