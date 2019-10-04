import unittest
from pencil import Pencil
from paper import Paper


class PencilWritingTests(unittest.TestCase):
    def setUp(self):
        self.pencil = Pencil()
        self.paper = Paper()

    def test_should_write_text_to_paper(self):
        text_to_write = 'abc'
        self.pencil.write(text_to_write, self.paper)
        self.assertEqual(self.paper.text, text_to_write)

    def test_should_append_text_to_end_of_paper(self):
        self.paper.text = 'abc'
        text_to_write = 'def'
        self.pencil.write(text_to_write, self.paper)
        self.assertEqual(self.paper.text, 'abcdef')


class PointDegradationTests(unittest.TestCase):
    def setUp(self):
        self.paper = Paper()

    def test_can_create_pencil_with_point_durability(self):
        pencil = Pencil(point_durability=0)
        self.assertEqual(pencil.point_durability, 0)

    def test_should_write_whitespace_if_point_durability_is_zero(self):
        pencil = Pencil(point_durability=0)
        text_to_write = 'abc'
        pencil.write(text_to_write, self.paper)
        self.assertEqual(self.paper.text, ' ' * len(text_to_write))
