class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def showcycle(self,head):
        i=0
        curr=self.head
        while i<100:
            print(curr.val,end="-->")
            curr=curr.next
            i=i+1
obj=linkedlist()
obj.head=Node(10)
obj.head.next=Node(20)
obj.head.next.next=Node(30)
obj.head.next.next.next=Node(40)
obj.head.next.next.next.next=obj.head.next
obj.showcycle(obj.head)
