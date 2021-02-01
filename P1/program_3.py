import sys

class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.next = None
        self.left = None
        self.right = None


class PriorityQueue:
    def __init__(self, node=None):
        self.start = node
        self.size = 0
        self.last = None

    def append(self, new_node):
        if not self.start:
            self.start = new_node 
            self.last = self.start

        else:
            self.last.next = new_node
            self.last = self.last.next

        self.size += 1

    def get_size(self):
        return self.size 

    def pop(self):
        if self.start:
            node = self.start
            self.start = self.start.next
            node.next = None
            self.size -= 1
            return node
        else:
            return

    def __str__(self):
        pv = ''
        node = self.start
        while node:
            pv += "[" + str(node.character) + ':' + str(node.frequency)+ '] --> '
            node = node.next
        return pv

def print_tree(tree):
    start = tree
    encoding_dict = {}

    encoding = ''
    queue = []

    keep_traversing = True
    
    tree_char = ''
    while keep_traversing:
        if start.left:
            queue.append(start.left)

        if start.right:
            queue.append(start.right)

        start = queue.pop(0)
        if start.character:
            tree_char += start.character + '  '

        if len(queue) == 0:
            keep_traversing = False

    print(tree_char)

def traverse_tree_get_encoding(tree):
    solution = {}
    if not tree:
        return None

    if tree.left and tree.left.character:
        solution[tree.left.character] = '0'

    else:
        left_sol = traverse_tree_get_encoding(tree.left)
        for each_key in left_sol:
            solution[each_key] = '0' + left_sol[each_key]

    if tree.right.character:
        solution[tree.right.character] = '1'
        
    else:
        right_sol = traverse_tree_get_encoding(tree.right)
        for each_key in right_sol:
            solution[each_key] = '1' + right_sol[each_key]

    return solution


def huffman_encoding(data):
    encoded_data, tree = '', None

    if data == '':
        return encoded_data, tree

    if len(data) == 1:
        tree = Node(None, 1)
        tree.left = Node(data, 1)
        return '0', tree

    data_new = data
    data_dict = {}
    for each_char in data_new:
        if each_char in data_dict:
            data_dict[each_char] += 1
        else:
            data_dict[each_char] = 1
    
    data_list = []
    for each_key in data_dict.keys():
        data_list.append(Node(each_key, data_dict[each_key]))

    data_list = sorted(data_list, key=lambda k: k.frequency)
    pq = PriorityQueue()
    while data_list:
        app = data_list.pop(0) 
        pq.append(app) 
 
    while pq.get_size() > 1:  
        first = pq.pop() 
        second = pq.pop() 

        new_freq = 0
        if first:
            new_freq += first.frequency

        if second:
            new_freq += second.frequency

        internal_node = Node(None, new_freq)
    
        internal_node.left = first
        internal_node.right = second 

        pq.append(internal_node)

    tree = pq.pop()
    encoding_dict = traverse_tree_get_encoding(tree)
    for each_char in data:
        encoded_data += encoding_dict[each_char]

    return encoded_data, tree
    

def huffman_decoding(data,tree):
    if data == '' or tree == None:
        return''

    start = tree
    return_value = ''
    data = list(data)

    while data:
        bit = data.pop(0)
        if bit == '0':
            start =  start.left

        elif bit == '1':
            start = start.right

        if start:
            # print("Node is: ", start.character, start.frequency, start.bit)
            if start.character:
                return_value += start.character
                start = tree

    return return_value

def test():
    # Test Cases
    codes = {}
    a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE" 
    encoded_data, tree = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree)  
    print ("Pass" if (a_great_sentence == decoded_data) else "Fail") 

    a_great_sentence = "The bird is the word" 
    encoded_data, tree = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree)  
    print ("Pass" if (a_great_sentence == decoded_data) else "Fail")
    

    a_great_sentence = "" 
    encoded_data, tree = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree) 
    print ("Pass" if (a_great_sentence == decoded_data) else "Fail")

    a_great_sentence = "A" 
    encoded_data, tree = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree) 
    print ("Pass" if (a_great_sentence == decoded_data) else "Fail")


if __name__ == "__main__":
    test()