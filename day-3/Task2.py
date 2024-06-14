class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    vals = []
    current = head
    while current:
        vals.append(current.val)
        current = current.next
    return vals == vals[::-1]

# Helper function to create a linked list from a list of values
def create_linked_list(vals):
    head = ListNode(vals[0])
    current = head
    for val in vals[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Test the is_palindrome function
vals = [1, 2, 3, 2, 1]
head = create_linked_list(vals)
if is_palindrome(head):
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")
