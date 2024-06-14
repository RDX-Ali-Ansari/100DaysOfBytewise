class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

# Helper function to create a linked list from a list of values
def create_linked_list(vals):
    head = ListNode(vals[0])
    current = head
    for val in vals[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    vals = []
    current = head
    while current:
        vals.append(current.val)
        current = current.next
    return ' -> '.join(map(str, vals))

# Test the reverse_linked_list function
vals = [1, 2, 3, 4, 5]
head = create_linked_list(vals)
reversed_head = reverse_linked_list(head)
print("Reversed linked list:", print_linked_list(reversed_head))
