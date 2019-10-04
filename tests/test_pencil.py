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
        durability=8
        pencil=Pencil(point_durability=8)
        pencil.write(to_write, self.paper)
        self.assertEqual(pencil.point_durability,durability-8)
