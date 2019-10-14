import unittest
from pencil_factory import PencilFactory


class Number2HBPencilFactoryTests(unittest.TestCase):
    def test_should_return_number_2hb_pencil(self):
        pencil = PencilFactory.get_no2_hb()

        self.assertEqual(pencil.point_durability,
                         PencilFactory.NO2_HB_POINT_DURABILITY)
        self.assertEqual(pencil.length, PencilFactory.NO2_HB_LENGTH)
        self.assertEqual(pencil.eraser.durability,
                         PencilFactory.NO2_HB_ERASER_DURABILITY)
