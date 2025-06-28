# Intersection of Two Linked Lists

This repository contains a Python solution for the [LeetCode problem "Intersection of Two Linked Lists"](https://leetcode.com/problems/intersection-of-two-linked-lists/).

##  Problem Description

You are given the heads of two singly linked lists, `headA` and `headB`.  
Return the node at which the two lists intersect.  
If the two linked lists have no intersection, return `None`.

##  Solution Approach

The solution first calculates the lengths of both lists.  
Then it moves the pointer of the longer list ahead by the length difference so that both pointers are equally far from the end.  
Finally, it advances both pointers together until they meet.

##  Steps:

1. Count the lengths of both linked lists.
2. Advance the longer list's pointer by the difference in lengths.
3. Traverse both lists together.
4. Return the first common node (by reference, not value).


##  Key Concepts Used

- Linked list traversal
- Pointer alignment
- Difference of lengths
- Space-efficient solution (no extra data structures used)

