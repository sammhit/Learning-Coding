class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,head,data): 
    #Complete this method
        current =head
        newNode = Node(data)
        newNode.next=None
        if(current!=None):
            while current.next!=None:
                current=current.next
            current.next=newNode    
                
        else:   
             head=newNode
        return head
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);   
