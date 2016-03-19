# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 12:27:50 2016

@author: abhibhat
"""
import functools
def find_max_sum(arr):
    """
    >>> find_max_sum([1, 2, 3, 4])
    6
    >>> find_max_sum([4, 1, 2])
    6
    >>> find_max_sum([4, 15, 2])
    15
    >>> find_max_sum([5, 5, 10, 100, 10, 5])
    110
    >>> find_max_sum([])
    0
    """
    if not arr: return 0
    incl, excl, excl_new  = arr[0], 0, 0
    for elem in arr[1:]:
        excl_new = incl if incl > excl else excl
        incl, excl = excl + elem, excl_new
    return incl if incl > excl else excl

def memoize(func):
    memo = {}
    @functools.wraps(func)
    def helper(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return helper
@memoize
def find_max_sumDP(arr):
    """
    >>> find_max_sumDP((1, 2, 3, 4))
    6
    >>> find_max_sumDP((4, 1, 2))
    6
    >>> find_max_sumDP((4, 15, 2))
    15
    >>> find_max_sumDP((5, 5, 10, 100, 10, 5))
    110
    >>> find_max_sumDP(())
    0
    """
    if len(arr) == 1:return arr[0]
    if not arr: return 0
    return max(max(arr[0] + find_max_sumDP(arr[2:]), find_max_sumDP(arr[2:])), 
               max(arr[1] + find_max_sumDP(arr[3:]), find_max_sumDP(arr[2:])))
           
if __name__ == "__main__":
    import doctest
    doctest.testmod()
