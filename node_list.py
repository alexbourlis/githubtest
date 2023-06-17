# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print_nodes(self):
        next_node = self
        list_val = []
        while(next_node != None):
            list_val.append(next_node.val)
            next_node = next_node.next
        print(list_val)
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head1, head2 = list1, list2
        node = ListNode()
        head = node
        while(head1 != None and head2 != None):
            if head1.val < head2.val:
                node.next = head1
                node = node.next
                head1 = head1.next
            else:
                node.next = head2
                node = node.next
                head2 = head2.next  
        node.next = head1 or head2
            
        return head.next

tail = ListNode(10)
head1 = tail
for i in range(8,-1,-2):
    new_node = ListNode(i)
    new_node.next = head1
    head1 = new_node

tail = ListNode(9)
head2 = tail
for i in range(7,-1,-2):
    new_node = ListNode(i)
    new_node.next = head2
    head2 = new_node

head1.print_nodes()
head2.print_nodes()

sol = Solution()
new_list_head = sol.mergeTwoLists(head1,head2)
new_list_head.print_nodes()



