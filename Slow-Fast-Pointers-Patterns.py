## Happy Number (LeetCode Problem-202)
class Solution:
    def isHappy(self, n: int) -> bool:

        def find_next_number(n):
            value = 0

            while n:
                digit = n % 10
                value += digit ** 2
                n = n // 10

            return value
        
        slow = n
        fast = find_next_number(n)

        while fast != 1 and slow != fast:
            slow = find_next_number(slow)
            fast = find_next_number(find_next_number(fast))

        return fast == 1

### Time Complexity -> O(n)
### Space Complexity -> O(1)

###########################################################
##  876. Middle of the Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
### Time Complexity -> O(n)
### Space Complexity -> O(1)


###########################################################
## 141. Linked List Cycle
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
       fast = head
       slow = head

       while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
    
       return False

### Time Complexity -> O(n)
### Space Complexity -> O(1)


###########################################################
## 142. Linked List Cycle II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        
        else: 
            return None

        lastNode = head

        while lastNode != slow:
            lastNode = lastNode.next
            slow = slow.next

        return slow

### Time Complexity -> O(n)
### Space Complexity -> O(1)



###########################################################

## 287. Find the Duplicate Number
def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow

### Time Complexity -> O(n)
### Space Complexity -> O(1)


###########################################################
## 234. Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        revs = None
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            revs, revs.next, slow = slow, revs, slow.next
        
        if fast:
            slow = slow.next
        while revs and revs.val == slow.val:
            slow = slow.next
            revs = revs.next

        return not revs



### Time Complexity -> O(n)
### Space Complexity -> O(1)