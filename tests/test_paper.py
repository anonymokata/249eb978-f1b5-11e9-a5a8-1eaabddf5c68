import unittest
from paper import Paper


class PaperCreationTests(unittest.TestCase):
    def test_should_instantiate_paper_with_empty_text_field(self):
        paper = Paper()
        self.assertIsInstance(paper, Paper)
        self.assertEqual(paper.text, '')

    def test_paper_text_should_be_set_with_text_property(self):
        paper = Paper()
        paper.text = 'abc'
        self.assertEqual(paper.text, 'abc')

    def test_can_initialize_paper_with_text(self):
        paper = Paper(initial_text='Hello Fellow')
        self.assertEqual(paper.text, 'Hello Fellow')

    def test_paper_should_initialize_last_erased_field(self):
        paper = Paper()
        self.assertEqual(paper.last_erased, -1)
