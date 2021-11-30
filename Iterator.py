class Unpacker:

    def __init__(self, very_packed_object):
        self.very_packed_object = very_packed_object
        self.step = 0
        self.packed_object = list()

    def __iter__(self):
        # Превращает начальный список в списко без вложенности
        # (Unpacker.very_packed_object --> Unpacker.packed_object)
        for unpacked_object in self.very_packed_object:
            for very_unpacked_object in unpacked_object:
                self.packed_object.append(very_unpacked_object)
        return self

    def __next__(self):
        try:
            next_item = self.packed_object[self.step]
            self.step += 1
            return next_item
        except IndexError:
            raise StopIteration


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

Unpacker_1 = Unpacker(nested_list)

for item in Unpacker_1:
    print(item)
