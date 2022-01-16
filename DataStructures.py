

from _typeshed import Self
from typing import Dict, Set


class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = max_size * [None]
        self.next_free_location = 0

    def push(self, item):
        if self.next_free_location == self.max_size:

            return False
        else:
            self.items[self.next_free_location]=item
            self.next_free_location += 1
            return True

    def pop(self):
        if self.next_free_location == 0:
            return None
        else:
            return_item = self.items[self.next_free_location-1]
            self.items[self.next_free_location-1] = None
            self.next_free_location -= 1
            return return_item

class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = max_size * [None]
        self.next_free_location = 0
        self.front_index = 0
    def enqueue(self, item):
        if self.next_free_location < self.max_size - 1:
            self.items[self.next_free_location] = item
            self.next_free_location += 1
            return True
        else:
            return False

    def dequeue(self):
        if self.next_free_location == self.front_index:
            return None
        else:
            return_item = self.items[self.front_index]
            self.items[self.front_index]=None
            self.front_index +=1
            return return_item
    
    def shuffle_items_forward_one_place(self):
        # If no space at the front then don't bother
        if self.front_index == 0:  
            return False
        
        # Otherwise, shift all items forward
        counter = self.front_index -1
        while counter < self.max_size - 2:
            self.items[counter] = self.items[counter + 1]
            counter += 1
        self.items[counter] = None
        self.front_index -= 1
        self.next_free_location -= 1
        return True    

class CircularQueue(Queue):
    def __init__(self, max_size):
        super().__init__(max_size)
    def enqueue(self, item):
        """Adds an item to the queue, or returns None"""
        # If something in next slot, can't do
        if self.items[self.next_free_location] != None:
            return False
        else:
            self.items[self.next_free_location] = item
            # TODO update next free location

            # TODO Make circular by wrapping around with mod

    def dequeue(self):
        return_item = self.items[self.front_index]
        self.items[self.front_index] = None
        # TODO update front index

        # TODO make circular
        self.front_index += 1
        self.front_index = self.front_index % self.max_size
        return return_item


class Node:
    def __init__(self, data : any) -> None:
        self.data = data
        self.children : Dict[Node, float] = {}
    def breadth_first_traversal(self) -> Set['Node']:
        if self.children == {}:
            return {}

        

class Tree:
    def __init__(self, root: Node)-> None:
        self.root = root

    def breadth_first_traversal(self) -> Set[Node]:
        return self.root.breadth_first_traversal()
        

def test_stack():
    ints = Stack(5)

    ints.push(2)
    ints.push(1)
    print(ints.items)
    ints.push(12)
    ints.push(11)
    ints.push(22)
    ints.push(112)
    ints.pop()
    ints.pop()
    print(ints.items)

def test_queue():
    ints = Queue(5)
    ints.enqueue(2)
    ints.enqueue(1)
    print(ints.items)
    ints.enqueue(12)
    ints.enqueue(11)
    ints.enqueue(22)
    ints.enqueue(112)
    ints.dequeue()
    ints.dequeue()
    print(ints.items)
    ints.shuffle_items_forward_one_place()
    print(ints.items)
    ints.shuffle_items_forward_one_place()
    print(ints.items)
    ints.shuffle_items_forward_one_place()
    print(ints.items)

def test_circular_queue():
    ints = CircularQueue(5)
    ints.enqueue(2)
    ints.enqueue(1)
    print(ints.items)
    ints.enqueue(12)
    ints.enqueue(11)
    ints.enqueue(22)
    ints.enqueue(112)
    print(ints.dequeue())
    print(ints.dequeue())
    print(ints.items)
    print(ints.enqueue(7))
    print(ints.items)
    print(ints.enqueue(-7))
    print(ints.items)
    print(ints.enqueue(-17))
    print(ints.dequeue())

test_stack()
test_queue()
test_circular_queue()
