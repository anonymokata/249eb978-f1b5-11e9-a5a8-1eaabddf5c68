import unittest
from paper import Paper

class PaperCreationTests(unittest.TestCase):
	def test_should_instantiate_paper_with_empty_text_field(self):
		paper = Paper()
		self.assertIsInstance(paper, Paper)
		self.assertEqual(paper.text, '')