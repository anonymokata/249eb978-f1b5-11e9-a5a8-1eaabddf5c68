class Paper:
    def __init__(self):
        self._text = ''
        self.last_erased=-1

    @property
    def text(self):
        return str(self._text)

    @text.setter
    def text(self, text):
        self._text = text
