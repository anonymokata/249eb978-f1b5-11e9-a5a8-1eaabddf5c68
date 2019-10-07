import unittest
from eraser import Eraser
from paper import Paper


class EraserEraseTests(unittest.TestCase):
    def setUp(self):
        self.paper = Paper(initial_text='ABC')
        self.eraser = Eraser(durability=1000)

    def test_eraser_should_erase_char_at_index(self):
        self.eraser.erase_char(paper=self.paper, index=1)
        self.assertEqual(self.paper.text, 'A C')

    def test_eraser_should_do_nothing_if_index_out_of_bounds(self):
        self.eraser.erase_char(self.paper, index=len(self.paper.text) + 100)
        
        
class Eraser_Degradation_Tests(unittest.TestCase):
    def setUp(self):
        self.paper = Paper(initial_text='ABC')
        self.eraser = Eraser(durability=1000)

    def test_erase_char_should_degrade_by_one_if_char_is_alphanum(self):
        initial_eraser_durability = self.eraser.durability
        self.eraser.erase_char(
            paper=self.paper, index=1)
        self.assertEqual(self.eraser.durability,
                         initial_eraser_durability - 1)

    def test_erase_char_should_degrade_by_one_if_char_is_alphanum(self):
        initial_eraser_durability = self.eraser.durability
        self.eraser.erase_char(
            paper=self.paper, index=self.paper.text.find('B'))
        self.assertEqual(self.eraser.durability,
                         initial_eraser_durability - 1)

    def test_erase_char_should_degrade_by_zero_if_char_is_space(self):
        initial_eraser_durability = self.eraser.durability
        self.paper.text = ' '
        self.eraser.erase_char(self.paper, 0)
        self.assertEqual(self.eraser.durability,
                         initial_eraser_durability)
