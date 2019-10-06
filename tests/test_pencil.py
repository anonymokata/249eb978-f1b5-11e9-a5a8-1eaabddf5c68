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
        self.assertEqual(self.paper.text, ' ' * len(text_to_write))

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
        pencil.write(' ', self.paper)
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
        self.assertEqual(self.paper.text, ' ')

    # Make note of this in Readme!
    def test_writing_a_number_should_use_two_units_of_durability(self):
        durability = 2
        pencil = Pencil(point_durability=2)
        pencil.write('1', self.paper)
        self.assertEqual(pencil.point_durability, durability - 2)

    def test_should_begin_writing_whitespace_midword_if_point_durability_is_zero(self):
        pencil = Pencil(point_durability=4)
        pencil.write('Text', self.paper)
        self.assertEqual(self.paper.text, 'Tex ')


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
        self.assertEqual(self.paper.text, (" " * len('Charles') + " Mingus"))

    def test_should_only_erase_last_occurence_of_text(self):
        self.paper.text = 'Hello Hello Hello'
        self.pencil.erase('Hello', self.paper)
        self.pencil.erase('Hello', self.paper)
        self.assertEqual(self.paper.text, 'Hello ' + ' ' *
                         len('Hello') + ' ' + ' ' * len('Hello'))

    def test_should_not_do_anything_if_paper_does_not_contain_text_to_erase(self):
        text = 'Mellow Yellow Fellow'
        self.paper.text = text
        self.pencil.erase('Buckingham', self.paper)
        self.assertEqual(self.paper.text, text)


class EraserDegradationTests(unittest.TestCase):
    def test_can_create_pencil_with_value_for_eraser_durability(self):
        durability=2000
        pencil = Pencil(eraser_durability=durability)
        self.assertEqual(pencil.eraser_durability, durability)
