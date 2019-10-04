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
        self.paper.text='abc'
        text_to_write='def'
        self.pencil.write(text_to_write, self.paper)
        self.assertEqual(self.paper.text, 'abcdef')
        