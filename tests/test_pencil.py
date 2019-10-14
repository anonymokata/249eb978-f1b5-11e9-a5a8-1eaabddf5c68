import unittest
from pencil import Pencil
from paper import Paper
from eraser import Eraser
import string
from unittest import skip
from pencil_factory import PencilFactory


class PencilWritingTests(unittest.TestCase):
    def setUp(self):
        self.pencil = PencilFactory.get_no2_hb()
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
        self.pencil = PencilFactory.get_no2_hb()
        self.initial_point_durability = self.pencil.point_durability

    def test_should_allow_creation_with_point_durability_field(self):
        self.assertEqual(self.pencil.point_durability,
                         PencilFactory.NO2_HB_POINT_DURABILITY)

    def test_should_write_whitespace_if_point_durability_is_zero(self):
        self.pencil.point_durability = 0
        text_to_write = 'abc'

        self.pencil.write(text_to_write, self.paper)

        self.assertEqual(
            self.paper.text, Pencil.SPACE_CHAR * len(text_to_write))

    def test_should_degrade_point_by_one_unit_when_writing_lowercase_char(self):
        self.pencil.write('a', self.paper)

        self.assertEqual(self.pencil.point_durability,
                         self.initial_point_durability - 1)

    def test_should_degrade_point_by_two_units_when_writing_uppercase_char(self):
        self.pencil.write('A', self.paper)

        self.assertEqual(self.pencil.point_durability,
                         self.initial_point_durability - 2)

    def test_should_not_degrade_point_when_writing_whitespace(self):
        self.pencil.write(Pencil.SPACE_CHAR, self.paper)

        self.assertEqual(self.pencil.point_durability,
                         self.initial_point_durability)

    def test_should_degrade_pencil_by_sum_of_characters_cost_units(self):
        #   2 cost units *2 uppercase chars
        # + 1 cost unit * 4 lowercase chars
        # + 0 cost units * 1 space
        # =8 cost units

        to_write = 'Abc Def'

        self.pencil.write(to_write, self.paper)

        self.assertEqual(self.pencil.point_durability,
                         self.initial_point_durability - 8)

    def test_should_not_write_uppercase_character_if_only_one_durability_unit(self):
        self.pencil.point_durability = 1

        self.pencil.write('A', self.paper)

        self.assertEqual(self.paper.text, Pencil.SPACE_CHAR)

    def test_should_degrade_two_units_when_writing_number(self):
        self.pencil.write('1', self.paper)

        self.assertEqual(self.pencil.point_durability,
                         self.initial_point_durability - 2)

    def test_should_begin_writing_whitespace_midword_if_point_durability_is_zero(self):
        self.pencil.point_durability = 4

        self.pencil.write('Text', self.paper)

        self.assertEqual(self.paper.text, ('Tex' + Pencil.SPACE_CHAR))


class PencilSharpeningTests(unittest.TestCase):
    def setUp(self):
        self.pencil = PencilFactory.get_no2_hb()
        self.initial_length = self.pencil.length

    def test_should_allow_creation_with_length(self):
        self.assertEqual(self.pencil.length, PencilFactory.NO2_HB_LENGTH)

    def test_should_reduce_length_by_one_when_sharpened(self):
        self.pencil.sharpen()

        self.assertEqual(self.pencil.length, self.initial_length - 1)

    def test_should_regain_original_point_durability_when_sharpened(self):
        initial_durability = self.pencil.point_durability
        self.pencil.point_durability = 0
        self.assertEqual(self.pencil.point_durability, 0)

        self.pencil.sharpen()

        self.assertEqual(self.pencil.point_durability, initial_durability)

    def test_should_not_restore_point_durability_when_sharpened_at_length_zero(self):
        self.pencil.length = 0
        self.pencil.point_durability = 1

        self.pencil.sharpen()

        self.assertEqual(self.pencil.point_durability, 1)


class PencilEditingTests(unittest.TestCase):

    def setUp(self):
        self.paper = Paper()
        self.pencil = PencilFactory.get_no2_hb()

    def test_should_append_to_end_of_paper_when_editing_if_paper_has_never_been_erased(self):
        self.paper.text = 'Hello '

        self.assertEqual(self.paper.last_erased, -1)

        self.pencil.edit('Fellow', self.paper)

        self.assertEqual(self.paper.text, 'Hello Fellow')

    def test_should_edit_text_into_whitespace_caused_by_last_erase(self):
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
            self.paper.text, f"An artich{Pencil.COLLISION_CHAR}k{Pencil.COLLISION_CHAR}ay keeps the doctor away")
