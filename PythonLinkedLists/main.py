# creating the list
class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class List(object):
    def __init__(self, head_node=None):
        self.head_node = head_node

    # this isn't strictly required, just allows the list to be printed
    def __str__(self):
        result = '['
        current_node = self.head_node
        is_first = True
        while current_node:
            if is_first:
                is_first = False
            else:
                result += ','
            result += str(current_node.value)
            current_node = current_node.next_node
        result += ']'
        return result

    def head(self):
        return self.head_node.value

    def tail(self):
        if self.is_empty():
            raise Exception('An empty list does not have a tail.')
        else:
            return List(self.head_node.next_node)

    # note that this is O(1)
    def prepend(self, value):
        new_head_node = Node(value, self.head_node)
        self.head_node = new_head_node

    # note that this is O(n)
    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head_node = new_node
        else:
            last_node = self.head_node

            while last_node.next_node:
                last_node = last_node.next_node

            last_node.next_node = new_node

    def is_empty(self):
        return self.head_node is None

# code to sum the list

def sum_list(object):
    if not object.is_empty():
        return object.head() + sum_list(object.tail())
    else:
        return 0

some_numbers = List()
some_numbers.prepend(3)
some_numbers.prepend(3)
some_numbers.prepend(4)
some_numbers.prepend(1)
some_numbers.prepend(7)
some_numbers.prepend(7)
some_numbers.prepend(1)
some_numbers.prepend(4)
some_numbers.prepend(5)
some_numbers.prepend(7)
print(sum_list(some_numbers))


# sumList :: (Num a) => [a] -> a
# sumList [] = 0
# sumList x = head x + sumList(tail x)

# main = print(sumList [7,5,4,1,7,7,1,4,3,3])