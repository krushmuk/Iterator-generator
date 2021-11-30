def unpacker(packed_list):
    for unpacked_list in packed_list:
        for unpacked_item in unpacked_list:
            yield unpacked_item


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]
for item in unpacker(nested_list):
    print(item)
