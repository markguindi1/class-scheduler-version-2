class UnsortedArrayMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    def __init__(self):
        self.table = []

    def __len__(self):
        return len(self.table)

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        for item in self.table:
            if(key == item.key):
                return item.value
        raise KeyError(str(key) + " is not in map")

    def __setitem__(self, key, value):
        for item in self.table:
            if (key == item.key):
                item.value = value
                return
        new_item = UnsortedArrayMap.Item(key, value)
        self.table.append(new_item)

    def __delitem__(self, key):
        for j in range(len(self.table)):
            if(key == self.table[j].key):
                self.table.pop(j)
                return
        raise KeyError(str(key) + " is not in map")

    def __iter__(self):
        for item in self.table:
            yield item.key



