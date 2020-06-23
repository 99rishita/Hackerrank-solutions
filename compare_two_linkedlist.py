#!/bin/python3

import os
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    ptr1 = llist1
    ptr2 = llist2
    while(ptr1!= None or ptr2!=None):
        if ptr1==None and ptr2!=None:
            return 0
        if ptr1!=None and ptr2==None:
            return 0
        if ptr1.data == ptr2.data:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        else:
            return 0
    return 1

if __name__ == '__main__':