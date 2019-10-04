class Pencil:

    def __init__(self, point_durability=40000):
        self._point_durability = point_durability

    @property
    def point_durability(self):
        return self._point_durability

    @point_durability.setter
    def point_durability(self, point_durability):
        self._point_durability = point_durability

    def write(self, text, paper):
        for char in text:
            self._write_char(char, paper)

    def _write_char(self, char, paper):
        if self.point_durability==0:
            paper.text+=' '
        else:
            if char.isupper():
                self.point_durability-=2
            elif char.islower():
                self.point_durability-=1
            paper.text+=char