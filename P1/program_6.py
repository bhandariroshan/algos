class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next

        out_string = out_string[0:-4]
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    set1 = set()
    set2 = set()

    node = llist_1.head
    while node != None:
        set1.add(node.value)
        node = node.next

    node = llist_2.head
    while node != None:
        set2.add(node.value)
        node = node.next

    unionset = set2.union(set1)
    union_ll = LinkedList()

    for each_elem in unionset:
        union_ll.append(each_elem)

    return union_ll

def intersection(llist_1, llist_2):
    set1 = set()
    set2 = set()

    node = llist_1.head
    while node != None:
        set1.add(node.value)
        node = node.next

    node = llist_2.head
    while node != None:
        set2.add(node.value)
        node = node.next

    unionset = set2.intersection(set1)
    inter_ll = LinkedList()

    for each_elem in unionset:
        inter_ll.append(each_elem)

    return inter_ll


def test():
    # Test Cases
    # Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    unl = union(linked_list_1,linked_list_2)
    inter = intersection(linked_list_1,linked_list_2)

    # 3 common elements
    print ("Pass" if (inter.size() == 3) else "Fail")

    # 11 total elements
    print ("Pass" if (unl.size() == 11) else "Fail")

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    unl = union(linked_list_3,linked_list_4)
    inter = intersection(linked_list_3,linked_list_4)

    # 3 common elements
    print ("Pass" if (inter.size() == 0) else "Fail")

    # 11 total elements
    print ("Pass" if (unl.size() == 13) else "Fail")    


    # Test case 3
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = []
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    unl = union(linked_list_3,linked_list_4)
    inter = intersection(linked_list_3,linked_list_4)

    # 3 common elements
    print ("Pass" if (inter.size() == 0) else "Fail")

    # 11 total elements
    print ("Pass" if (unl.size() == 6) else "Fail")


    # Test case 4
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    unl = union(linked_list_3,linked_list_4)
    inter = intersection(linked_list_3,linked_list_4)

    # 3 common elements
    print ("Pass" if (inter.size() == 0) else "Fail")

    # 11 total elements
    print ("Pass" if (unl.size() == 0) else "Fail")

if __name__ == "__main__":
    test()