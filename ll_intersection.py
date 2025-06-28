class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA, headB):
        lenA = 0
        lenB = 0
        currentA = headA
        currentB = headB

        while currentA:
            lenA += 1
            currentA = currentA.next

        while currentB:
            lenB += 1
            currentB = currentB.next

        currentA = headA
        currentB = headB
        diff = abs(lenA - lenB)

        if lenA > lenB:
            for _ in range(diff):
                currentA = currentA.next
        else:
            for _ in range(diff):
                currentB = currentB.next

        while currentA is not currentB:
            currentA = currentA.next
            currentB = currentB.next

        return currentA
