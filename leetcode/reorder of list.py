class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def reorderList(self, head):
        # Finding the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Divide the linked list into two halves
        h2 = slow.next
        tail = slow.next = None

        # Reverse the second half of the linked list
        while h2:
            temp = h2.next
            h2.next = tail
            tail = h2
            h2 = temp

        # Merge two halves of the linked list
        h1, h2 = head, tail
        while h2:
            temp1, temp2 = h1.next, h2.next
            h1.next = h2
            h2.next = temp1
            h1, h2 = temp1, temp2

    def show(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")

obj = linkedlist()
obj.head = Node(10)
obj.head.next = Node(20)
obj.head.next.next = Node(30)
obj.head.next.next.next = Node(40)
obj.head.next.next.next.next = Node(50)
obj.show()
obj.reorderList(obj.head)
obj.show()

