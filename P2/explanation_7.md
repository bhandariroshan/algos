# RouteTrieNode --> insert 
lets say there are n words that we need to insert. This time, we are using whole word as a key. Inserting a element in dictionary is O(1) in time complexity.  The Trie node stores a word  as key and then ChildrenNode as value. The children RouteTrieNode is initially storing nothing and has a variable to store handler and default handler value. These all require constant space. Hence it is O(1) in space complexity.


# RouteTrie --> insert
We need to insert n words. Using the RuoteTrieNode insert and in RoteTrieNode is O(1) time complexity. Since there are n elements that needs to be inserted, overall time complexity of this part would be O(n) in time and space.

# RouteTrie --> Find
To find a path list of n elements, first we have to check the first element in the root node and then if matchecd, we have to keep looking for the children and their nodes. If the path is existing each of the elements in the path list would form a nested children list like that in linkedlist. So we might have to do  1 + 2 + 3 + ...n checks to find n elements. Hence the overall time complexity of the code is O(n^2) in time. Since there are only 1 variable needed to store the value if exists or not, overall space complexity of the code will be O(1) in space.

# Router --> split
This function takes a string of length m and splits the it into a list of word seperated by "/". Lets say there are n words. Then at worst case it has to traverse all those m characters or n words, keep parsing and store them in a new list. So the overall complexity of this code is O(n) in time and space both considering n words in the string.

# Router --> add_handler
This function takes path string and splits it which is O(n) in time and space both. Then for each word it inserts into routetrie. Since all of these words has to be formed as such each word that comes after one in list has to be children in the RouteTrieNode. As such the time and space compleixty of this code would be O(n) in both time and space.

# Router --> lookup
The lookup function takes path sting and splits it into a list. The split function has O(n) time and space complexity. At worst case all the elements in the list would be nested children to each other. To look for the word, it implements find. The find function has O(n) time and O(1) space complexity. For n elements it has do 1 + 2 + 3 + 4 + ...... + n searches. So the overall time complexity of this part would be O(n^2). Since only one variable is needed to store the handler so the space complexity will be O(1).