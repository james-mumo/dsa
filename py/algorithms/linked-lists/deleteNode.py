class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def addEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode

    def displayNodes(self):
        if self.head is None:
            print("Empty")
        else:
            curr = self.head
            while curr:
                print(curr.data, end=" -> ")
                curr = curr.next
            print()

    def delEnd(self):
        if self.head is None:
            print("Empty List")
        else:
            curr = self.head
            prev = None
            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = None

    def delStart(self):
        if self.head is None:
            print("Empty List")
            return
        else:
            self.head = self.head.next

    def delMid(self, target):
        if self.head is None:
            print("Empty List")
            return
        if self.head.data == target:
            self.head = self.head.next
        else:
            curr = self.head
            prev = None
            while curr:
                if curr.data == target:
                    prev.next = curr.next
                prev = curr
                curr = curr.next
            print("Item not found")

    def delete_at_position(self, pos):
        if pos < 0:
            print("Invalid position")
            return
        elif self.head is None:
            print("List is empty")
            return
        else:
            curr = self.head
            prev = None
            count = 0
            while curr and count < pos:
                prev = curr
                count += 1
                curr = curr.next
                if curr is None:

            #         if we get to the end
            prev.next = curr.next


ll = Linkedlist()
ll.addEnd(5)
ll.addEnd(4)
ll.addEnd(3)
ll.addEnd(2)
ll.addEnd(1)
ll.displayNodes()
ll.delete_at_position(1)
ll.displayNodes()
ll.delEnd()
ll.displayNodes()
ll.delStart()
ll.displayNodes()
ll.delMid(5)
ll.displayNodes()
ll.delete_at_position(3)
ll.displayNodes()
