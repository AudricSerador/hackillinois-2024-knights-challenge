import unittest
from main import get_max_goodness

class TestGetMaxGoodness(unittest.TestCase):
    def test_one_component_1(self):
        nodes = {
            "a": 5,
            "b": 3,
            "c": 1,
            "d": 4,
            "e": 2,
        }
        edges = [
            ["a", "b"],
            ["b", "c"],
            ["c", "d"],
            ["d", "e"],
        ]
        self.assertEqual(get_max_goodness(nodes, edges), 15)

    def test_one_component_2(self):
        nodes = {
            "e": 2,
            "d": 4,
            "c": 1,
            "b": 3,
            "a": 5,
        }
        edges = [
            ["e", "d"],
            ["d", "c"],
            ["c", "b"],
            ["b", "a"],
        ]
        self.assertEqual(get_max_goodness(nodes, edges), 15)

    def test_multiple_components_1(self):
        nodes = {
            "a": 20,
            "b": 30,
            "c": 2,
            "d": 3,
            "e": -100,
        }
        edges = [
            ["a", "c"],
            ["b", "d"],
        ]
        self.assertEqual(get_max_goodness(nodes, edges), 33)

    def test_multiple_components_2(self):
        nodes = {
            "e": -100,
            "d": 3,
            "c": 2,
            "b": 30,
            "a": 20,
        }
        edges = [
            ["e", "c"],
            ["b", "d"],
        ]
        self.assertEqual(get_max_goodness(nodes, edges), 33)

    def test_varying_edge_components_1(self):
        nodes = {
            "a": 10,
            "b": 9,
            "c": 8,
            "d": 7,
            "e": 6,
            "f": 5,
            "g": 4,
            "h": 3,
            "i": 2,
            "j": 1,
        }
        edges = [
            ["a", "b"],
            ["c", "d"],
            ["e", "f"],
            ["g", "h"],
            ["i", "j"],
        ]
        self.assertEqual(get_max_goodness(nodes, edges), 19)

    def test_varying_edge_components_2(self):
        nodes = {
            "j": 1,
            "i": 2,
            "h": 3,
            "g": 4,
            "f": 5,
            "e": 6,
            "d": 7,
            "c": 8,
            "b": 9,
            "a": 10,
        }
        edges = [
            ["j", "i"],
            ["h", "g"],
            ["f", "e"],
            ["d", "c"],
            ["b", "a"],
        ]
        self.assertEqual(get_max_goodness(nodes, edges), 19)

if __name__ == '__main__':
    unittest.main()