#!/bin/python3
# https://www.hackerrank.com/challenges/30-binary-search-trees/problem?isFullScreen=true
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
    def getHeight(self,root):
        ans = 0
        queue = collections.deque()
        if root is None:
            return ans
        queue.append(root)
        while queue:
            currSize = len(queue)
            # Unless the queue is empty
            while currSize > 0:
                # Pop elements one-by-one
                currNode = queue.popleft()
                currSize -= 1
    
                # Check if the node has left/right child
                if currNode.left is not None:
                    queue.append(currNode.left)
                if currNode.right is not None:
                    queue.append(currNode.right)
    
            # Increment ans when currSize = 0
            ans += 1
        return ans - 1  # hackerrank fix ¯\_(ツ)_/¯

import collections
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
