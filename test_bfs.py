import unittest
from part2Task1 import *





class TestBFS(unittest.TestCase):
    def test1(self):
        """BFS test 1 (2 point)"""
        m = [('UPS', 'Brecon', 3), ('Jacob City', 'Owl Ranch', 3), ('Jacob City', 'Sunfield', 15), ('Sunfield', 'Brecon', 25)]
        val = bfs(m, 'UPS')
        expected = {'UPS':['UPS'],'Brecon':['UPS', 'Brecon'], 'Sunfield':['UPS', 'Brecon', 'Sunfield'], 'Jacob City':['UPS', 'Brecon', 'Sunfield', 'Jacob City'], 'Owl Ranch':['UPS', 'Brecon', 'Sunfield', 'Jacob City', 'Owl Ranch']}
        self.assertEqual(val, expected)

    def test2(self):
        """BFS test 2 (2 point)"""
        m = [('UPS', 'Brecon', 28), ('UPS', 'Owl Ranch', 20), ('UPS', 'Sunfield', 17), ('Jacob City', 'Brecon', 25), ('Sunfield', 'Owl Ranch', 0)]
        val = bfs(m, 'UPS')
        expected = {'UPS':['UPS'],'Brecon':['UPS', 'Brecon'], 'Sunfield':['UPS', 'Sunfield'], 'Jacob City':['UPS', 'Brecon', 'Jacob City'], 'Owl Ranch':['UPS', 'Owl Ranch']}
        self.assertEqual(val, expected)

    def test3(self):
        """BFS test 3 (2 point)"""
        m = [('UPS', 'Brecon', 17), ('UPS', 'Jacob City', 17), ('UPS', 'Owl Ranch', 4), ('Sunfield', 'Brecon', 11), ('Owl Ranch', 'Sunfield', 10), ('Jacob City', 'Sunfield', 0)]
        val = bfs(m, 'UPS')
        expected = {'UPS': ['UPS'], 'Brecon': ['UPS', 'Brecon'], 'Jacob City': ['UPS', 'Jacob City'], 'Owl Ranch': ['UPS', 'Owl Ranch'], 'Sunfield': ['UPS', 'Brecon', 'Sunfield']}
        self.assertEqual(val, expected)

    def test4(self):
        """BFS test 4 (2 point)"""
        m = [('UPS', 'Steuben', 22), ('Richmond Hill', 'Steuben', 22), ('Richmond Hill', 'Hambleton', 18), ('Richmond Hill', 'Owl Ranch', 18), ('Holly Ridge', 'Diehlstadt', 3), ('Holly Ridge', 'Jacob City', 0), ('Holly Ridge', 'Steuben', 17), ('Diehlstadt', 'Brecon', 8), ('Diehlstadt', 'Hambleton', 9), ('Diehlstadt', 'Steuben', 11), ('Steuben', 'Hambleton', 13), ('Steuben', 'Brecon', 25), ('Hambleton', 'Jacob City', 1), ('Jacob City', 'Sunfield', 19), ('Jacob City', 'Brecon', 1), ('Sunfield', 'Brecon', 12)]
        val = bfs(m, 'UPS')
        expected = {'UPS': ['UPS'], 'Steuben': ['UPS', 'Steuben'], 'Richmond Hill': ['UPS', 'Steuben', 'Richmond Hill'], 'Hambleton': ['UPS', 'Steuben', 'Hambleton'], 'Owl Ranch': ['UPS', 'Steuben', 'Richmond Hill', 'Owl Ranch'], 'Holly Ridge': ['UPS', 'Steuben', 'Holly Ridge'], 'Diehlstadt': ['UPS', 'Steuben', 'Diehlstadt'], 'Jacob City': ['UPS', 'Steuben', 'Brecon', 'Jacob City'], 'Brecon': ['UPS', 'Steuben', 'Brecon'], 'Sunfield': ['UPS', 'Steuben', 'Brecon', 'Sunfield']}
        self.assertEqual(val, expected)

    def test5(self):
        """BFS test 5 (2 point)"""
        m = [('UPS', 'Steuben', 15), ('Richmond Hill', 'Steuben', 20), ('Richmond Hill', 'Owl Ranch', 17), ('Richmond Hill', 'Diehlstadt', 27), ('Richmond Hill', 'Sunfield', 22), ('Richmond Hill', 'Holly Ridge', 13), ('Holly Ridge', 'Sunfield', 16), ('Holly Ridge', 'Hambleton', 17), ('Holly Ridge', 'Jacob City', 13), ('Holly Ridge', 'Owl Ranch', 0), ('Holly Ridge', 'Steuben', 17), ('Holly Ridge', 'Diehlstadt', 0), ('Jacob City', 'Owl Ranch', 13), ('Sunfield', 'Brecon', 24)]
        val = bfs(m, 'UPS')
        expected = {'UPS': ['UPS'], 'Steuben': ['UPS', 'Steuben'], 'Richmond Hill': ['UPS', 'Steuben', 'Richmond Hill'], 'Owl Ranch': ['UPS', 'Steuben', 'Holly Ridge', 'Owl Ranch'], 'Diehlstadt': ['UPS', 'Steuben', 'Holly Ridge', 'Diehlstadt'], 'Sunfield': ['UPS', 'Steuben', 'Holly Ridge', 'Sunfield'], 'Holly Ridge': ['UPS', 'Steuben', 'Holly Ridge'], 'Hambleton': ['UPS', 'Steuben', 'Holly Ridge', 'Hambleton'], 'Jacob City': ['UPS', 'Steuben', 'Holly Ridge', 'Jacob City'], 'Brecon': ['UPS', 'Steuben', 'Holly Ridge', 'Sunfield', 'Brecon']}
        self.assertEqual(val, expected)

test = TestBFS()

test.test1()
test.test2()
test.test3()
test.test4()
test.test5()
