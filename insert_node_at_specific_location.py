#!/bin/python3

import math
import os
import random
import re
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

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    count = 0
    prev = head
    current = head
    new_node = SinglyLinkedListNode(data)
    if position == 0:
        new_node.next = head
        head = new_node
        return head
    while(count<=position):
        if count == position:
            prev.next = new_node
            new_node.next = current
            return head
        else:
            prev = current
            current = current.next
            count += 1
    return head
    

if __name__ == '__main__':