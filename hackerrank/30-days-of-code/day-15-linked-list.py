#!/bin/python3
#https://www.hackerrank.com/challenges/30-linked-list/problem?isFullScreen=true
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

    def insert(self, head, data): 
        if head is None:
            self.nodes = []
            self.nodes.append(Node(data))
            return self.nodes[-1]
        current = head
        previous = head
        while current:
            previous = current
            current = current.next
        self.nodes.append(Node(data))
        previous.next = self.nodes[-1]
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  
