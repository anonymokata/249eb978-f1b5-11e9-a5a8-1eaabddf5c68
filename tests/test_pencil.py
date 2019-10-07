import unittest
from pencil import Pencil
from paper import Paper
import string
from unittest import skip


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


class PencilPointDegradationTests(unittest.TestCase):

    def setUp(self):
        self.paper = Paper()

    def test_can_create_pencil_with_point_durability(self):
        pencil = Pencil(point_durability=0)
        self.assertEqual(pencil.point_durability, 0)

    def test_should_write_whitespace_if_point_durability_is_zero(self):
        pencil = Pencil(point_durability=0)
        text_to_write = 'abc'
        pencil.write(text_to_write, self.paper)
        self.assertEqual(self.paper.text, Pencil.SPACE * len(text_to_write))

    def test_should_degrade_point_by_one_unit_when_writing_lowercase_char(self):
        durability = 1
        pencil = Pencil(point_durability=durability)
        pencil.write('a', self.paper)
        self.assertEqual(pencil.point_durability, durability - 1)

    def test_should_degrade_point_by_two_units_when_writing_uppercase_char(self):
        durability = 2
        pencil = Pencil(point_durability=durability)
        pencil.write('A', self.paper)
        self.assertEqual(pencil.point_durability, durability - 2)

    def test_should_not_degrade_point_when_writing_whitespace(self):
        durability = 1
        pencil = Pencil(point_durability=durability)
        pencil.write(Pencil.SPACE, self.paper)
        self.assertEqual(pencil.point_durability, durability)

    def test_should_degrade_pencil_by_sum_of_characters_cost_units(self):
        #   2 cost units *2 uppercase chars
        # + 1 cost unit * 4 lowercase chars
        # + 0 cost units * 1 space
        # =8 cost units

        to_write = 'Abc Def'
        durability = 8
        pencil = Pencil(point_durability=8)
        pencil.write(to_write, self.paper)
        self.assertEqual(pencil.point_durability, durability - 8)

    def test_should_not_write_uppercase_character_if_only_one_durability_unit(self):
        pencil = Pencil(point_durability=1)
        pencil.write('A', self.paper)
        self.assertEqual(self.paper.text, Pencil.SPACE)

    # Make note of this in Readme!
    def test_writing_a_number_should_use_two_units_of_durability(self):
        durability = 2
        pencil = Pencil(point_durability=2)
        pencil.write('1', self.paper)
        self.assertEqual(pencil.point_durability, durability - 2)

    def test_should_begin_writing_whitespace_midword_if_point_durability_is_zero(self):
        pencil = Pencil(point_durability=4)
        pencil.write('Text', self.paper)
        self.assertEqual(self.paper.text, 'Tex' + Pencil.SPACE)


class PencilSharpeningTests(unittest.TestCase):

    def test_pencil_should_have_length_field(self):
        initial_length = 40
        pencil = Pencil(length=initial_length)
        self.assertEqual(pencil.length, initial_length)

    def test_sharpening_pencil_should_reduce_its_length_by_one(self):
        initial_length = 40
        pencil = Pencil(length=initial_length)
        pencil.sharpen()
        self.assertEqual(pencil.length, initial_length - 1)

    def test_sharpening_pencil_should_restore_its_original_point_durability(self):
        initial_durability = 40000
        pencil = Pencil(point_durability=initial_durability, length=40)
        pencil.point_durability = 0
        self.assertEqual(pencil.point_durability, 0)

        pencil.sharpen()

        self.assertEqual(pencil.point_durability, initial_durability)

    def test_should_not_restore_point_durability_when_sharpened_with_length_zero(self):
        pencil = Pencil(point_durability=40000, length=0)
        pencil.point_durability = 1
        pencil.sharpen()
        self.assertEqual(pencil.point_durability, 1)


class PencilEraserTests(unittest.TestCase):
    def setUp(self):
        self.paper = Paper()
        self.pencil = Pencil()

    def test_should_erase_text_by_replacing_with_empty_spaces(self):
        self.paper.text = "Charles Mingus"
        self.pencil.erase("Charles", self.paper)
        self.assertEqual(self.paper.text, (Pencil.SPACE *
                                           len('Charles') + " Mingus"))

    def test_should_only_erase_last_occurence_of_text(self):
        self.paper.text = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"

        self.pencil.erase('chuck', self.paper)
        self.assertEqual(
            self.paper.text, "How much wood would a woodchuck chuck if a woodchuck could       wood?")

        self.pencil.erase('chuck', self.paper)
        self.assertEqual(
            self.paper.text, "How much wood would a woodchuck chuck if a wood      could       wood?")

    def test_should_not_do_anything_if_paper_does_not_contain_text_to_erase(self):
        text = 'Mellow Yellow Fellow'
        self.paper.text = text
        self.pencil.erase('Buckingham', self.paper)
        self.assertEqual(self.paper.text, text)

    def test_should_erase_char_should_erase_single_char_at_index(self):
        self.paper.text = 'ABC'
        self.pencil._erase_char(
            paper=self.paper, index=self.paper.text.find('B'))
        self.assertEqual(self.paper.text, 'A C')

    def test_erase_char_should_degrade_by_one_if_char_is_alphanum_else_zero(self):
        initial_eraser_durability = self.pencil.eraser_durability
        self.paper.text = 'ABC'
        self.pencil._erase_char(
            paper=self.paper, index=self.paper.text.find('B'))
        self.assertEqual(self.pencil.eraser_durability,
                         initial_eraser_durability - 1)


class EraserDegradationTests(unittest.TestCase):

    def setUp(self):
        self.initial_eraser_durability = 2000
        self.pencil = Pencil(eraser_durability=self.initial_eraser_durability)
        self.paper = Paper()

    def test_can_create_pencil_with_value_for_eraser_durability(self):
        pencil = Pencil(eraser_durability=self.initial_eraser_durability)
        self.assertEqual(pencil.eraser_durability,
                         self.initial_eraser_durability)

    def test_erasing_one_character_should_degrade_eraser_by_one(self):
        self.paper.text = 'A'
        self.pencil.erase('A', self.paper)
        self.assertEqual(self.pencil.eraser_durability,
                         self.initial_eraser_durability - 1)

    def test_erasing_two_characters_should_degrade_eraser_by_two(self):
        self.paper.text = 'AA'
        self.pencil.erase('AA', self.paper)
        self.assertEqual(self.pencil.eraser_durability,
                         self.initial_eraser_durability - 2)

    def test_erasing_whitespace_should_not_degrade_eraser(self):
        self.paper.text = string.whitespace
        self.pencil.erase(string.whitespace, self.paper)
        self.assertEqual(self.pencil.eraser_durability,
                         self.initial_eraser_durability)

    def test_should_erase_text_right_to_left(self):
        self.paper.text = 'Buffalo Bill'
        self.pencil.eraser_durability = 3
        self.pencil.erase('Bill', self.paper)
        self.assertEqual(self.paper.text, 'Buffalo B' + 3 * Pencil.SPACE)


class PencilEditingTests(unittest.TestCase):
    def setUp(self):
        self.pencil = Pencil()
        self.paper = Paper()

    def test_paper_should_initialize_last_erased_field(self):
        paper = Paper()
        self.assertEqual(paper.last_erased, -1)

    def test_pencil_should_set_last_erased_field_when_erasing(self):
        text = 'ABC'
        self.paper.text = text
        self.pencil.erase('B', self.paper)
        self.assertEqual(self.paper.last_erased, 1)

    def test_pencil_should_set_last_erased_to_last_character_erased_if_eraser_wears_out(self):
        self.pencil.eraser_durability = 2
        text = 'ABC'
        self.paper.text = text
        self.pencil.erase('ABC', self.paper)
        self.assertEqual(self.paper.last_erased, 1)

    def test_if_paper_has_not_had_text_erased_should_append_text_to_paper(self):
        self.paper.text = 'Hello '
        self.assertEqual(self.paper.last_erased, -1)
        self.pencil.edit('Fellow', self.paper)
        self.assertEqual(self.paper.text, 'Hello Fellow')

    def test_pencil_should_edit_text_into_whitespace_caused_by_last_erase(self):
        self.paper.text = 'An apple a day keeps the doctor away'
        self.pencil.erase('apple', self.paper)
        self.pencil.edit('onion', self.paper)
        self.assertEqual(
            self.paper.text, 'An onion a day keeps the doctor away')

    def test_should_reflect_collision_when_edited_in_text_is_longer_than_erased_whitespace(self):
        self.paper.text = 'An apple a day keeps the doctor away'
        self.pencil.erase('apple', self.paper)
        self.pencil.edit('artichoke', self.paper)
        self.assertEqual(
            self.paper.text, f"An artich{Pencil.COLLISION}k{Pencil.COLLISION}ay keeps the doctor away")
