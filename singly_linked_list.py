class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def list_size(self):
        temp = self.head
        while temp is not None:
            self.count += 1
            temp = temp.next
        return self.count

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def append(self, val):
        temp = self.head

        if temp is None:
            temp = Node(val)
            self.head = temp
            return

        last = None

        while temp.next is not None:
            last = temp
            temp = temp.next

        temp.next = Node(val)
        return

    def iter_nodes(self, root):
        temp = root

        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

    def recur_nodes(self, root):
        if root is None:
            return

        print(root.data)
        self.recur_nodes(root.next)


    def reverse_nodes(self, root):
        temp = None
        head = root

        while head is not None:
            temp2 = head.next
            head.next = temp
            temp = head
            head = temp2

        self.head = temp

    def swap_nodes(self, node, x, y):
        if x == y:
            return

        prevx = None
        curx = node
        while curx is not None and curx.data != x:
            prevx = curx
            curx = curx.next

        prevy = None
        cury = node
        while cury is not None and cury.data != y:
            prevy = cury
            cury = cury.next

        if curx is None or cury is None:
            return

        if prevx:
            prevx.next = cury
        else:
            self.head = cury

        if prevy:
            prevy.next = curx
        else:
            self.head = curx

        curx.next, cury.next = cury.next, curx.next

    def sort_nodes(self, node):
        if self.count < 0:
            return

        temp = node
        while temp.next is not None:
            if temp.data > temp.next.data:
                temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next
        self.count = self.count - 1
        self.sort_nodes(node)

    def get_pos(self, node, val):
        temp = node
        i = 0
        while temp is not None:
            if temp.data == val:
                return i
            i += 1
            temp = temp.next

        return "No such value"

    def update_val(self, node, prev_val, new_val):
        temp = node
        while temp is not None:
            if temp.data == prev_val:
                temp.data = new_val
                return
            temp = temp.next

        return "No such value"

    def del_node(self, node, val):
        temp = node
        last = None

        if temp.data == val:
            nn = temp.next
            del temp
            self.head = nn
            return
        else:
            while temp is not None:
                if temp.next.data == val:
                    last = temp.next
                    break
                temp = temp.next

        temp.next = last.next
        del last


ll = LinkedList()

ll.head = Node(10)

ll.append(4)
ll.append(19)
ll.append(2)
ll.append(5)
ll.append(1)
ll.append(7)
ll.append(456)

ll.iter_nodes(ll.head)
