#-*- coding: utf-8 -*-
'''
2016-08-22
Kevin Cantú

Variations of the grain counting functions for a clever person's chessboard
'''


### a rough little memoization decorator


from functools import wraps


def memoize(func):
    results = {}

    @wraps(func)
    def wrapper(ii):
        if not ii in results:
            results[ii] = func(ii)
        else:
            print 'using memoized value for ii: %s' % ii
        return results[ii]
    return wrapper


### recursive implementation


@memoize
def on_square(ii):
    '''
    Given the square index (from one to sixty-four), calculate all the earlier squares and
    return the number of grains on this one.
    '''
    if ii <= 0:
        # The servant isn't referring to square zero!  (Tests from exercism confirm this.)
        raise IndexError('Chessboard indexing starts with 1, sorry!')
    if ii >= 65:
        # We don't want to think about unreasonably large chessboards, or recursion depth, yet.
        raise IndexError('Chessboard indexing ends with 64, sorry!')
    if ii == 1:
        # initial square
        return 1
    # subsequent squares
    return 2*on_square(ii-1)


@memoize
def total_after(jj):
    '''
    Given the square index (from one to sixty-four) so far --
    assuming this suqare and previous ones are filled, and subsequent ones are empty --
    return how many grains are on the board.
    '''
    all_squares = [on_square(kk+1) for kk in range(jj)]
    return sum(all_squares)


### recursion-free implementation


def list_squares_norec_zero(ii):
    '''
    Given a square index (from one to N), calculate the grains on this and previous squares.

    Warning: the list returned will be zero-indexed: 0 is square 1.

    TODO: make this use something memoize-able for sub-lists?
    '''
    if ii == 0:
        # The servant isn't referring to square zero!  (Tests from exercism confirm this.)
        raise IndexError('Chessboard indexing starts with 1, sorry!')

    all_squares = []
    for ll in range(ii):
        if ll == 0:
            all_squares.append(1)
        else:
            all_squares.append(2 * all_squares[-1])
    return all_squares


def on_square_norec(ii):
    '''
    Given the square index (from one to N), calculate all the earlier squares and
    return the number of grains on this one.
    '''
    all_squares = list_squares_norec_zero(ii)
    return all_squares[-1]


def total_after_norec(jj):
    '''
    Given the square index (from one to N) so far --
    assuming this suqare and previous ones are filled, and subsequent ones are empty --
    return how many grains are on the board.
    '''
    all_squares = list_squares_norec_zero(jj)
    return sum(all_squares)
