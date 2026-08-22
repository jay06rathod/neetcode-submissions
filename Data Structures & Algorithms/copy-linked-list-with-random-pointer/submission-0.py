"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        hashmap = {}
        current = head

        while current:
            hashmap[current] = Node(current.val)
            current = current.next
        
        current = head

        while current:
            copy = hashmap[current]
            copy.next = hashmap.get(current.next)
            copy.random = hashmap.get(current.random)

            current = current.next

        return hashmap[head]