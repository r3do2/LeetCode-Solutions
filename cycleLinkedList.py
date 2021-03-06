''' Cycle in a linked LIST 
 head -> NULL id LIST is empty '''
  
 # cheacking for cycle method

def has_cycle(head):
    if (head == None):
        return False
    else:
        slow = head
        fast = head.next
        while (slow != fast) :
            if (fast == None or fast.next == None):
                return False
            else:
                slow = slow.next;
                fast = fast.next.next;
        return True
