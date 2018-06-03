class Empty(Exception):
    pass

class ArrayMinHeap:
    class Item:
        def __init__(self, priority, value):
            self.priority = priority
            self.value = value

    def __init__(self, priority_list=None, values_list=None):
        self.data = [None]
        if (priority_list is not None):
            for i in range(len(priority_list)):
                self.data.append(ArrayMinHeap.Item(priority_list[i],
                                                   values_list[i]))
            first_non_leaf_ind = self.parent(len(self.data) - 1)
            for ind in range(first_non_leaf_ind, 0, -1):
                self.fix_down(ind)

    def __len__(self):
        return len(self.data) - 1

    def is_empty(self):
        return (len(self) == 0)

    def left(self, i):
        return i*2

    def right(self, i):
        return i*2 + 1

    def parent(self, i):
        return i//2

    def min(self):
        if (self.is_empty()):
            raise Empty("Priority queue is empty")
        item = self.data[1]
        return (item.priority, item.value)


    def insert(self, priority, value):
        new_item = ArrayMinHeap.Item(priority, value)
        self.data.append(new_item)
        self.fix_up(len(self.data) - 1)

    def fix_up(self, i):
        parent_ind = self.parent(i)
        if(i > 1 and self.data[i].priority < self.data[parent_ind].priority):
            self.swap(i, parent_ind)
            self.fix_up(parent_ind)

    def swap(self, i1, i2):
        self.data[i1], self.data[i2] = self.data[i2], self.data[i1]


    def delete_min(self):
        if(self.is_empty()):
            raise Empty("Priority queue is empty")
        self.swap(1, len(self.data) - 1)
        item = self.data.pop()
        self.fix_down(1)
        return (item.priority, item.value)

    def fix_down(self, i):
        if (self.has_left(i)):
            left_ind = self.left(i)
            smaller_child = left_ind
            if (self.has_right(i)):
                right_ind = self.right(i)
                if (self.data[right_ind].priority < self.data[smaller_child].priority):
                    smaller_child = right_ind
            if (self.data[i].priority > self.data[smaller_child].priority):
                self.swap(i, smaller_child)
                self.fix_down(smaller_child)

    def has_left(self, i):
        left_ind = self.left(i)
        return (left_ind <= len(self.data) - 1)

    def has_right(self, i):
        right_ind = self.right(i)
        return (right_ind <= len(self.data) - 1)


def heap_sort(lst):
    n = len(lst)
    heap = ArrayMinHeap(lst, [None]*n)
    res_lst = []
    for i in range(n):
        (priority, value) = heap.delete_min()
        res_lst.append(priority)
    return res_lst
