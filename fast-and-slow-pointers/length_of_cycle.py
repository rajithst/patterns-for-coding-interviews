class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# fast and slow pointer to check if cycle exisit
def find_cycle_length(head):
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # if cycle found,try to find the length of the cycle
        if slow == fast:
            return calculate_length(slow)
    return 0


def calculate_length(slow):
    current = slow
    length = 0
    # define one of pointer as starting point of the cycle(slow or fast)
    # move another pointer forward till meet the starting point,while moving calculate the length
    while True:
        current = current.next
        length += 1
        if current == slow:
            break
    return length


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print(find_cycle_length(head))


if __name__ == '__main__':
    main()
