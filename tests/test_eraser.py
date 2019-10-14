import unittest
from eraser import Eraser
from paper import Paper
import string


class EraseTests(unittest.TestCase):

    def setUp(self):
        self.paper = Paper()
        self.eraser = Eraser(durability=1000)

    # tests _erase_char method
    def test_should_erase_char_at_index(self):
        self.paper.text = 'ABC'
        
        self.eraser._erase_char(paper=self.paper, index=1)
        
        self.assertEqual(self.paper.text, 'A C')

    # tests _erase_char method
    def test_should_do_nothing_if_index_out_of_bounds(self):
        self.paper.text = 'ABC'
        
        self.eraser._erase_char(self.paper, index=len(self.paper.text) + 1)
        
        self.assertEqual(self.paper.text, 'ABC')

    def test_should_erase_text_by_replacing_with_empty_spaces(self):
        self.paper.text = "Charles Mingus"
        
        self.eraser.erase("Charles", self.paper)
        
        self.assertEqual(self.paper.text, (Eraser.ERASE_CHAR *
                                           len('Charles') + " Mingus"))

    def test_should_only_erase_last_occurence_of_text(self):
        self.paper.text = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"

        self.eraser.erase('chuck', self.paper)
        
        self.assertEqual(
            self.paper.text, "How much wood would a woodchuck chuck if a woodchuck could       wood?")

        self.eraser.erase('chuck', self.paper)
        
        self.assertEqual(
            self.paper.text, "How much wood would a woodchuck chuck if a wood      could       wood?")

    def test_should_not_do_anything_if_paper_does_not_contain_text_to_erase(self):
        text = 'Stevie Nicks'
        self.paper.text = text
        
        self.eraser.erase('Lindsey Buckingham', self.paper)
        
        self.assertEqual(self.paper.text, text)

    def test_should_erase_text_right_to_left(self):
        self.paper.text = 'Buffalo Bill'
        self.eraser.durability = 3
        
        self.eraser.erase('Bill', self.paper)
        
        self.assertEqual(self.paper.text, 'Buffalo B' +
                         (3 * Eraser.ERASE_CHAR))

    def test_should_set_last_erased_field_when_erasing(self):
        self.paper.text = 'ABC'
        
        self.eraser.erase('B', self.paper)
        
        self.assertEqual(self.paper.last_erased, 1)

    def test_should_set_last_erased_to_last_character_erased_if_eraser_wears_out_while_erasing(self):
        self.eraser.durability = 2
        self.paper.text = 'ABC'
        
        self.eraser.erase('ABC', self.paper)
        
        self.assertEqual(self.paper.last_erased, 1)


class EraserDegradationTests(unittest.TestCase):
    def setUp(self):
        self.initial_eraser_durability = 1000
        self.paper = Paper()
        self.eraser = Eraser(durability=self.initial_eraser_durability)

    def test_should_degrade_by_one_if_char_is_alphanum(self):
        initial_eraser_durability = self.eraser.durability
        self.paper.text = 'A'
        
        self.eraser._erase_char(
            paper=self.paper, index=0)
        
        self.assertEqual(self.eraser.durability,
                         initial_eraser_durability - 1)

    def test_should_degrade_by_zero_if_char_is_space(self):
        initial_eraser_durability = self.eraser.durability
        self.paper.text = ' '
        
        self.eraser._erase_char(self.paper, 0)
        
        self.assertEqual(self.eraser.durability,
                         initial_eraser_durability)

    def test_should_degrade_by_two_when_erasing_two_characters(self):
        self.paper.text = 'AA'
        
        self.eraser.erase('AA', self.paper)
        
        self.assertEqual(self.eraser.durability,
                         self.initial_eraser_durability - 2)

    def test_should_not_degrade_when_erasing_Whitespace(self):
        self.paper.text = string.whitespace
        
        self.eraser.erase(string.whitespace, self.paper)
        
        self.assertEqual(self.eraser.durability,
                         self.initial_eraser_durability)
