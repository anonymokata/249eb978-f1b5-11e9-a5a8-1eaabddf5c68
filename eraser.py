from pencil import Pencil


class Eraser:
    ERASE_CHAR=' '
    
    def __init__(self, durability):
        self.durability = durability

    def erase(self,text,paper):
        index = paper.text.rfind(text)

        if index < 0:
            return

        # Step backward from the end of text to be erased
        for i in range(len(text) - 1, -1, -1):
            self._erase_char(paper, index + i)

    def _erase_char(self, paper, index):
        if self.durability == 0 or index>=len(paper.text):
            return

        self.durability -= self._calculate_erase_cost(paper.text[index])
        paper.text = paper.text[:index] + Pencil.SPACE_CHAR + paper.text[index + 1:]
        paper.last_erased = index

    def _calculate_erase_cost(self, char):
        if char.isspace():
            return 0
        else:
            return 1
