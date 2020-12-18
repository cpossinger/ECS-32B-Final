import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility
from part2Task1 import *



class TestDFS(unittest.TestCase):
    @weight(5)
    def test1(self):
        """DFS test 1 (2 point)"""
        m = [('UPS', 'Brecon', 3), ('Jacob City', 'Owl Ranch', 3), ('Jacob City', 'Sunfield', 15), ('Sunfield', 'Brecon', 25)]
        val = dfs(m, 'UPS')
        expected = {'UPS': ['UPS'], 'Brecon': ['UPS', 'Brecon'], 'Jacob City': ['UPS', 'Brecon', 'Sunfield', 'Jacob City'], 'Owl Ranch': ['UPS', 'Brecon', 'Sunfield', 'Jacob City', 'Owl Ranch'], 'Sunfield': ['UPS', 'Brecon', 'Sunfield']}
        self.assertEqual(val, expected)

    @weight(5)
    def test2(self):
        """DFS test 2 (2 point)"""
        m = [('UPS', 'Brecon', 28), ('UPS', 'Owl Ranch', 20), ('UPS', 'Sunfield', 17), ('Jacob City', 'Brecon', 25), ('Sunfield', 'Owl Ranch', 0)]
        val = dfs(m, 'UPS')
        expected = {'UPS': ['UPS'], 'Brecon': ['UPS', 'Brecon'], 'Owl Ranch': ['UPS', 'Sunfield', 'Owl Ranch'], 'Sunfield': ['UPS', 'Sunfield'], 'Jacob City': ['UPS', 'Brecon', 'Jacob City']}
        self.assertEqual(val, expected)

    @weight(5)
    def test3(self):
        """DFS test 3 (2 point)"""
        m = [('UPS', 'Brecon', 17), ('UPS', 'Jacob City', 17), ('UPS', 'Owl Ranch', 4), ('Sunfield', 'Brecon', 11), ('Owl Ranch', 'Sunfield', 10), ('Jacob City', 'Sunfield', 0)]
        val = dfs(m, 'UPS')
        expected = {'UPS': ['UPS'], 'Brecon': ['UPS', 'Owl Ranch', 'Sunfield', 'Brecon'], 'Jacob City': ['UPS', 'Owl Ranch', 'Sunfield', 'Jacob City'], 'Owl Ranch': ['UPS', 'Owl Ranch'], 'Sunfield': ['UPS', 'Owl Ranch', 'Sunfield']}
        self.assertEqual(val, expected)

    @weight(5)
    def test4(self):
        """DFS test 4 (2 point)"""
        m = [('UPS', 'Steuben', 22), ('Richmond Hill', 'Steuben', 22), ('Richmond Hill', 'Hambleton', 18), ('Richmond Hill', 'Owl Ranch', 18), ('Holly Ridge', 'Diehlstadt', 3), ('Holly Ridge', 'Jacob City', 0), ('Holly Ridge', 'Steuben', 17), ('Diehlstadt', 'Brecon', 8), ('Diehlstadt', 'Hambleton', 9), ('Diehlstadt', 'Steuben', 11), ('Steuben', 'Hambleton', 13), ('Steuben', 'Brecon', 25), ('Hambleton', 'Jacob City', 1), ('Jacob City', 'Sunfield', 19), ('Jacob City', 'Brecon', 1), ('Sunfield', 'Brecon', 12)]
        val = dfs(m, 'UPS')
        expected = {'UPS': ['UPS'], 'Steuben': ['UPS', 'Steuben'], 'Richmond Hill': ['UPS', 'Steuben', 'Richmond Hill'], 'Hambleton': ['UPS', 'Steuben', 'Richmond Hill', 'Hambleton'], 'Owl Ranch': ['UPS', 'Steuben', 'Richmond Hill', 'Owl Ranch'], 'Holly Ridge': ['UPS', 'Steuben', 'Richmond Hill', 'Hambleton', 'Jacob City', 'Sunfield', 'Brecon', 'Diehlstadt', 'Holly Ridge'], 'Diehlstadt': ['UPS', 'Steuben', 'Richmond Hill', 'Hambleton', 'Jacob City', 'Sunfield', 'Brecon', 'Diehlstadt'], 'Jacob City': ['UPS', 'Steuben', 'Richmond Hill', 'Hambleton', 'Jacob City'], 'Brecon': ['UPS', 'Steuben', 'Richmond Hill', 'Hambleton', 'Jacob City', 'Sunfield', 'Brecon'], 'Sunfield': ['UPS', 'Steuben', 'Richmond Hill', 'Hambleton', 'Jacob City', 'Sunfield']}
        self.assertEqual(val, expected)

    @weight(5)
    def test5(self):
        """DFS test 5 (2 point)"""
        m = [('UPS', 'Steuben', 15), ('Richmond Hill', 'Steuben', 20), ('Richmond Hill', 'Owl Ranch', 17), ('Richmond Hill', 'Diehlstadt', 27), ('Richmond Hill', 'Sunfield', 22), ('Richmond Hill', 'Holly Ridge', 13), ('Holly Ridge', 'Sunfield', 16), ('Holly Ridge', 'Hambleton', 17), ('Holly Ridge', 'Jacob City', 13), ('Holly Ridge', 'Owl Ranch', 0), ('Holly Ridge', 'Steuben', 17), ('Holly Ridge', 'Diehlstadt', 0), ('Jacob City', 'Owl Ranch', 13), ('Sunfield', 'Brecon', 24)]
        val = dfs(m, 'UPS')
        expected = {'UPS': ['UPS'], 'Steuben': ['UPS', 'Steuben'], 'Richmond Hill': ['UPS', 'Steuben', 'Richmond Hill'], 'Owl Ranch': ['UPS', 'Steuben', 'Richmond Hill', 'Sunfield', 'Holly Ridge', 'Owl Ranch'], 'Diehlstadt': ['UPS', 'Steuben', 'Richmond Hill', 'Sunfield', 'Holly Ridge', 'Diehlstadt'], 'Sunfield': ['UPS', 'Steuben', 'Richmond Hill', 'Sunfield'], 'Holly Ridge': ['UPS', 'Steuben', 'Richmond Hill', 'Sunfield', 'Holly Ridge'], 'Hambleton': ['UPS', 'Steuben', 'Richmond Hill', 'Sunfield', 'Holly Ridge', 'Hambleton'], 'Jacob City': ['UPS', 'Steuben', 'Richmond Hill', 'Sunfield', 'Holly Ridge', 'Owl Ranch', 'Jacob City'], 'Brecon': ['UPS', 'Steuben', 'Richmond Hill', 'Sunfield', 'Brecon']}
        self.assertEqual(val, expected)
