from paper import Paper


class Pencil:
    SPACE = ' '
    COLLISION = '@'

    def __init__(self, point_durability=40000, length=40, eraser=None):
        self.point_durability = point_durability
        self.length = length
        self.initial_durability = point_durability
        self.eraser = eraser

    def write(self, text, paper):
        for char in text:
            self._write_char(char, len(paper.text), paper)

    def _write_char(self, char, index, paper):

        if self.point_durability < self._calculate_write_cost(char):
            char = Pencil.SPACE
        elif self._is_collision(index, paper):
            char = Pencil.COLLISION

        self.point_durability -= self._calculate_write_cost(char)
        paper.text = paper.text[:index] + char + paper.text[index + 1:]

    def _is_collision(self, index, paper):
        return not index > len(paper.text) - 1 and not paper.text[index].isspace()

    def _calculate_write_cost(self, char):
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
        self.eraser.erase(text, paper)
        
    def edit(self, text, paper):
        index = paper.last_erased

        if index == -1:
            self.write(text, paper)
            return

        for char in text:
            self._write_char(char, index, paper)
            index += 1
