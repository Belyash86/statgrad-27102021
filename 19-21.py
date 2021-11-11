from functools import lru_cache
def moves(h):
    a = h
    return a+1, a*3

@lru_cache(None)
def game(h):
    if h >= 46: return 'W'
    if any(game(x) == 'W' for x in moves(h)): return 'P1'
    if all(game(x) == 'P1' for x in moves(h)): return 'V1'
    if any(game(x) == 'V1' for x in moves(h)): return 'P2'
    if all(game(x) == 'P1' or game(x) == 'P2' for x in moves(h)): return 'V2'

for s in range(1, 45+1):
    g = game(s)
    if g != None:
        print(s, g)