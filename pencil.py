from paper import Paper


class Pencil:
    SPACE = ' '
    COLLISION = '@'

    def __init__(self, point_durability=40000, length=40, eraser_durability=4000):
        self.point_durability = point_durability
        self.length = length
        self.initial_durability = point_durability
        self.eraser_durability = eraser_durability

    def write(self, text, paper):
        for char in text:
            self.write_char(char, paper)

    def write_char(self, char, paper):
        if self.calculate_write_cost(char) > self.point_durability:
            paper.text += Pencil.SPACE
        else:
            self.point_durability -= self.calculate_write_cost(char)
            paper.text += char

    def calculate_write_cost(self, char):
        if char.isupper() or char.isnumeric():
            return 2
        elif char.islower():
            return 1
        else:
            return 0

    def sharpen(self):
        if self.length == 0:
            return

        self.point_durability = self.initial_durability
        self.length -= 1

    def erase(self, text, paper):
        index = paper.text.rfind(text)

        if index < 0:
            return

        # Step backward from the end of text to be erased
        for i in range(len(text) - 1, -1, -1):
            self._erase_char(paper, index + i)

    def _erase_char(self, paper, index):
        if self.eraser_durability == 0:
            return
        self.eraser_durability -= self._calculate_erase_cost(paper.text[index])
        paper.text = paper.text[:index] + Pencil.SPACE + paper.text[index + 1:]
        paper.last_erased = index

    def _calculate_erase_cost(self, char):
        if char.isspace():
            return 0
        else:
            return 1

    def edit(self, text, paper):
        index = paper.last_erased

        if index == -1:
            self.write(text, paper)
            return

        for char in text:
            self._write_char(char, index, paper)
            index += 1
