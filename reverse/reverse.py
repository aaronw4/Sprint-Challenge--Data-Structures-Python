class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is None:
            return None
        elif node.get_next() is None:
            return node.value
        else:
            curr_node = node
            arr = []
            while curr_node:
                arr.append(curr_node)
                curr_node = curr_node.get_next()
            while len(arr) != 0:
                new_node = arr.pop(0)
                self.add_to_head(new_node.value)
            

        # else:
        #     prev = None
        #     curr = node
        #     next = node.get_next()

        #     while next:
        #         curr.set_next(prev)
        #         next.set_next(curr)
        #         prev = curr
        #         curr = next
        #         next = curr.get_next()
        #         if next is None:
        #             self.head = curr
        #         return self
       