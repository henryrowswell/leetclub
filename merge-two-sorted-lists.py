'''
https://leetcode.com/problems/merge-two-sorted-lists/
1) Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __str__(self):
        return "{}-->{}".format(self.val, self.next)

def createListNodeFromArray(arr):
    rootNode = ListNode('start')
    currentNode = rootNode
    for el in arr:
        currentNode.next = ListNode(el)
        currentNode = currentNode.next
    
    return rootNode.next
        

class Solution1(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        resultRoot = ListNode('start')
        resultTail = resultRoot
        while (l1 != None and l2 != None):
            if l1.val < l2.val:
                # add l1
                resultTail.next = l1
                resultTail = resultTail.next
                l1 = l1.next
            elif l1.val == l2.val:
                # add l1
                resultTail.next = l1
                resultTail = resultTail.next
                l1 = l1.next

                # add l2
                resultTail.next = l2
                resultTail = resultTail.next
                l2 = l2.next
            elif l1.val > l2.val:
                # add l2
                resultTail.next = l2
                resultTail = resultTail.next
                l2 = l2.next
        
        if l1 != None:
            resultTail.next = l1
        
        if l2 != None:
            resultTail.next = l2
        

        return resultRoot.next # return without "start" node
    
    # def test(self, l1, l2, expectation):
    #     assert(self.mergeTwoLists(l1, l2) == expectation)
    
    def deepEquality(self, l1, l2):
        if l1 == None and l2 == None:
            return True
        
        while l1 != None:
            if l1.val == l2.val:
                l1 = l1.next
                l2 = l2.next
                continue
            else:
                return False
        
        # l1 is None
        if l2 != None:
            return False
        else:
            return True
        
    def test(self, l1, l2, expectation):
        got = self.mergeTwoLists(l1, l2)
        result = self.deepEquality(got, expectation)

        if result:
            print('passed:', got, expectation)
        else:
            print('failed:', got, expectation)
    
    def runTests(self):
        self.test(None, None, None)

        self.test(None, ListNode(1), ListNode(1))

        self.test(ListNode(1), None, ListNode(1))

        self.test(ListNode(2), ListNode(1), createListNodeFromArray([1,2]))

        self.test(createListNodeFromArray([1,3,5,5,6,8]), createListNodeFromArray([1,2,7,8,9]), createListNodeFromArray([1,1,2,3,5,5,6,7,8,8,9]))


s1 = Solution1()
s1.runTests()