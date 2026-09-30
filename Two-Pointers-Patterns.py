### 1.Two Sum II - Input Array Is Sorted

def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            k = numbers[i] + numbers[j]

            if (k > target):
                j = j - 1
            elif (k < target):
                i = i + 1
            else:
                return [i + 1, j + 1]
        return []


### Time Complexity -> O(n)
### Space Complexity -> O(1)

###########################################################

### 2. Merge Sorted Array

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

### Time Complexity -> O(m + n)
### Space Complexity -> O(1)

###########################################################

### 3. Valid Palindrome

def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        def is_alphanumeric(ch):
            code = ord(ch)
            return (48 <= code <= 57) or (65 <= code <= 90) or (97 <= code <= 122)

        while i < j:
            left = s[i]
            right =  s[j]

            if not is_alphanumeric(left):
                i += 1
                continue

            if not is_alphanumeric(right):
                j -= 1
                continue

            if left.lower() != right.lower():
                return False

            i += 1
            j -= 1

        return True
        
### Time Complexity -> O(n)
### Space Complexity -> O(n)

###########################################################

### 4. Count Pairs Whose Sum is Less than Target

def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()

        i = 0
        j = len(nums) - 1
        count = 0

        while i < j:
            if nums[i] + nums[j] < target:
                count +=  j - i
                i += 1
            else:
                j = j - 1

        return count

### Time Complexity -> O(nlogn)
### Space Complexity -> O(n)

###########################################################

### 5. 3 Sum

def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                val = nums[i] + nums[j] + nums[k]

                if val > 0:
                    k -= 1
                elif val < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res


### Time Complexity -> O(n2)
### Space Complexity -> O(n)

###########################################################

### 6. Remove Nth Node From End of List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        d = ListNode(0, head)
        l = d
        r = head

        while n > 0 and r:
            r = r.next
            n -= 1
        
        while r:
            l = l.next
            r = r.next

        l.next = l.next.next

        return d.next

### Time Complexity -> O(n)
### Space Complexity -> O(1)



###########################################################

### 6. Reverse Words in a String

def reverseWords(self, s: str) -> str:
        words = s.split()
        res = []

        for i in range(len(words) - 1, -1, -1):
            res.append(words[i])
            if i != 0:
                res.append(" ")
        
        return "".join(res)


### Time Complexity -> O(n)
### Space Complexity -> O(n)
        