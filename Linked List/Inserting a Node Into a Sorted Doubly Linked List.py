#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)
 
def sortedInsert(head, data):
    newnode=DoublyLinkedListNode(data)
    cur=head
    while((cur!=None) and (cur.data<data)):
        temp=cur#if cur become none i.e we traverse full llist so to get the last element
        cur=cur.next
    #if we have to add node at the beginning    
    if(cur==head):
        newnode.next=head
        head.prev=newnode
        head=newnode
    #if we have to ad the node at the end    
    elif(cur==None):
        temp.next=newnode
        newnode.prev=temp
    #normal case    
    else:
        temp.next=newnode
        newnode.prev=temp
        cur.prev=newnode
        newnode.next=cur
    return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
