import random

random.seed(0)

# Stacks with Array
# class Stack:
#     def __init__(self, rang=5):
#         self.arr = []
#         self.top = -1
#         self.rang = rang
#
#     def spush(self, val):
#         if self.top > self.rang:
#             print("Cannot push item, limit: ", self.rang)
#             return
#         self.top += 1
#         self.arr.append(val)
#         return
#
#     def spop(self, val):
#         if self.top < -1:
#             print("No more items to pop!")
#             return
#
#         self.top -= 1
#         index = 0
#         for i in self.arr:
#             if i == val:
#                 break
#             index += 1
#
#         self.arr.pop(index)
#         return
#
#     def display(self):
#         return self.arr
#
#     def topEle(self):
#         return self.arr[self.top]
#
#
# s = Stack(6)
#
# for i in range(5):
#     r = random.randint(0, 100)
#     s.spush(r)
#
# s.spop(49)
#
# print(s.display())
# print("Top element: ", s.topEle())


# Stacks with LinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.root = None

    def push(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return

        new_node.next = self.root
        self.root = new_node
        return

    def display(self):
        temp = self.root
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

    def pop(self):
        if self.root is None:
            return
        else:
            self.root = self.root.next

    def search_pop(self, val):
        temp = self.root
        prev = None

        if self.root.data == val:
            prev = self.root.next
            self.root = prev
            return

        while temp.next is not None:
            if temp.next.data == val:
                prev = temp
                temp = temp.next
                break
            temp = temp.next

        prev.next = temp.next
        temp = prev
        return

    def topEle(self):
        return self.root.data


s = Stack()

s.root = Node(1)
s.push(4)
s.push(7)
s.push(9)
s.push(10)


s.display()



