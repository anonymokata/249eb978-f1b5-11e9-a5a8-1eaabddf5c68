import unittest
from pencil import Pencil 
from paper import Paper
class PencilWritingTests(unittest.TestCase):
	def test_should_write_text_to_paper(self):
		text_to_write='abc'
		pencil = Pencil()
		paper= Paper()
		pencil.write(text_to_write, paper)
		self.assertEqual(paper.text, text_to_write)