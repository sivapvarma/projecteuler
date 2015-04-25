#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Siva Prasad Varma

import csv
from heapq import heappush, heappop
import doctest


# Constants
inf = float('inf')

def solve(W):
    """
    >>> W = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150],
    ... [630, 803, 746, 422, 111], [537, 699, 497, 121, 956],
    ... [805, 732, 524, 37, 331]]
    >>> solve(W)
    Minimum Sum path cost: 2297
    """
    # setup dijkstra
    h, w = len(W), len(W[0])
    D, P = dijsktra(W, (0,0))
    print('Minimum Sum path cost: {}'.format(D[(h-1, w-1)]))

def dijsktra(W, s):
    # Dijkstra algorithm for single source shortest path
    h, w = len(W), len(W[0])
    D, P, Q, S = {s:W[s[0]][s[1]]}, {}, [(W[0][0], s)], set()
    while Q:
        _, u = heappop(Q)       # Node with lowest estimate
        if u in S: continue
        S.add(u)
        for v in neighbours(u, h, w):
            relax(W, u, v, D, P)
            heappush(Q, (D[v], v))
    return D, P

def neighbours(u, h, w):
    x, y = u
    if x > 0:
        yield (x-1, y)
    if x+1 < h:
        yield (x+1, y)
    if y > 0:
        yield (x, y-1)
    if y +1 < w:
        yield (x, y+1)


def relax(W, u, v, D, P):
    d = D.get(u, inf) + W[v[0]][v[1]] # cost of edge is dependent only on v
    if d < D.get(v, inf):
        D[v], P[v] = d, u
        return True

if __name__ == '__main__':
    doctest.testmod()
    # read the matrix from text file
    W = []
    with open('..\data\p083_matrix.txt') as f:
        reader = csv.reader(f)
        for row in reader:
            W.append(list(map(int, row)))
    print('h, w = {}, {}'.format(len(W), len(W[0])))
    solve(W)
