class PrintObjects:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def print(self):
        return self

print_objects = PrintObjects(34)
print(print_objects)
