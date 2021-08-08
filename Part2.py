from _typeshed import Self


class Dictionary:
    def __init__(self):
        self.records = dict()
    def add(self, record):
        self.records[record] = self.records.get(record, 0) + 1
dictionary = Dictionary()
dictionary.add("python")
dictionary.add("hi")
print(dictionary.records)