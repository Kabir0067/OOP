class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length


rect = Rectangle(5, 3)
print(f"Initial length: {rect.length}")

rect.length = 10
print(f"Updated length: {rect.length}")