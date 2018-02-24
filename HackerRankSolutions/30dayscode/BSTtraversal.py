import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def levelOrder(self,root):
        #Write your code here
        self.queue = []
        if root!=None:
            self.queue.append(root)
            while(self.queue):
                root=self.queue.pop(0)
                print(root.data,end=' ')
                if root.left!=None:
                    self.queue.append(root.left)
                if root.right!=None:
                    self.queue.append(root.right)
            
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

