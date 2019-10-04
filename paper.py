class Paper:
	def __init__(self):
		self._text=''

	@property
	def text(self):
		return str(self._text)

	@text.setter
	def text(self, text):
		self._text=text
