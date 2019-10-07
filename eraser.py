from pencil import Pencil


class Eraser:
    def __init__(self, durability):
        self.durability = durability

    def erase_char(self, paper, index):
        if self.durability == 0 or index>=len(paper.text):
            return

        self.durability -= self.calculate_erase_cost(paper.text[index])
        paper.text = paper.text[:index] + Pencil.SPACE + paper.text[index + 1:]
        paper.last_erased = index

    def calculate_erase_cost(self, char):
        if char.isspace():
            return 0
        else:
            return 1
