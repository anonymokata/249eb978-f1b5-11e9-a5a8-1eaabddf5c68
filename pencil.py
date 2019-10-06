from paper import Paper
class Pencil:
    SPACE=' '
    def __init__(self, point_durability=40000, length=40, eraser_durability=4000):
        self._point_durability = point_durability
        self._length = length
        self._initial_durability = point_durability
        self._eraser_durability = eraser_durability

    @property
    def eraser_durability(self):
        return self._eraser_durability

    @eraser_durability.setter
    def eraser_durability(self, durability):
        self._eraser_durability = durability

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    @property
    def point_durability(self):
        return self._point_durability

    @point_durability.setter
    def point_durability(self, point_durability):
        self._point_durability = point_durability

    def write(self, text, paper):
        for char in text:
            self.write_char(char, paper)

    def write_char(self, char, paper):
        if self.calculate_char_write_cost(char) > self.point_durability:
            paper.text += Pencil.SPACE
        else:
            self.point_durability -= self.calculate_char_write_cost(char)
            paper.text += char

    def calculate_char_write_cost(self, char):
        if char.isupper() or char.isnumeric():
            return 2
        elif char.islower():
            return 1
        else:
            return 0

    def sharpen(self):
        if self.length == 0:
            return

        self.point_durability = self._initial_durability
        self.length -= 1

    def erase(self, text, paper):
        index = paper.text.rfind(text)

        if index < 0:
            return

        paper.text = paper.text[:index] + Pencil.SPACE * \
            len(text) + paper.text[len(text) + index:]

        self.eraser_durability -= self.calculate_erase_cost(text)

    def calculate_erase_cost(self, text):
        erase_cost = 0
        for char in text:
            if not char.isspace():
                erase_cost += 1
        return erase_cost
