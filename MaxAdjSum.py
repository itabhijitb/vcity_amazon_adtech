# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 12:27:50 2016

@author: abhibhat
"""

def find_max_sum(arr):
    """
    find_max_sum([1, 2, 3, 4])
    >> 6
    find_max_sum([4, 2])
    >> 6
    find_max_sum([4, 15, 2])
    >> 15
    find_max_sum([5, 5, 10, 100, 10, 5])
    >> 110
    find_max_sum([])
    >> 0
    """
    incl, excl, excl_new  = arr[0], 0, 0
    for elem in arr[1:]:
        excl_new = incl if incl > excl else excl
        incl, excl = excl + elem, excl_new
    return incl if incl > excl else excl
              
if __name__ == "__main__":
    import doctest
    doctest.testmod()
