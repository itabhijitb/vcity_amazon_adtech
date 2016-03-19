# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 13:11:18 2016

@author: abhibhat
"""
import unittest
from collections import Counter



class website_analyzer(object):
    def __init__(self):
        self.counter = Counter()

    def report_page_access(self, page_url):
        self.counter[page_url] += 1

    def get_top_npages(self, n):
        from operator import itemgetter
        return map(itemgetter(0), self.counter.most_common(n))

class website_analyzer_test(unittest.TestCase):
    def testnum(self):
        wa = website_analyzer()
        data = [2, 1, 10, 3, 4, 4, 2, 5, 10, 1, 3, 4, 5]
        for elem in data:
            wa.report_page_access(elem)
        self.assertEqual(wa.get_top_npages(3), [4, 1, 2])
        
    def testst(self):
        wa = website_analyzer()
        data = ['2', '1', '10', '3', '4', '4', '2', '5', 
                '10', '1', '3', '4', '5']
        for elem in data:
            wa.report_page_access(elem)
        self.assertEqual(wa.get_top_npages(3), ['4', '10', '1'])
        
    def test_eg1(self):
        wa = website_analyzer()
        data = []
        for elem in data:
            wa.report_page_access(elem)
        self.assertEqual(wa.get_top_npages(3), [])
        
    def test_eg2(self):
        wa = website_analyzer()
        data =  [2, 1, 10, 3, 4, 4, 2, 5, 10, 1, 3, 4, 5]
        for elem in data:
            wa.report_page_access(elem)
        self.assertEqual(wa.get_top_npages(0), [])
        
if __name__ == '__main__':
    unittest.main()
