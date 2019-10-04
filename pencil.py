class Pencil:

    def __init__(self, point_durability=None):
        self._point_durability = point_durability

    @property
    def point_durability(self):
        return self._point_durability

    @point_durability.setter
    def point_durability(self,point_durability):
        self._point_durability=point_durability

    def write(self, text, paper):
        if self.point_durability == 0:
            paper.text += ' ' * len(text)
        else:
            paper.text += text
