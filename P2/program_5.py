#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node 
# which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  
# To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes 
# that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` 
# and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, 
# collecting suffixes as you go.)

# In[77]:


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        if self.children == {}:
            return ['']
        
        
        return_res = []
        if self.is_word:
            return_res.append('')
        
        for eachkey in self.children:
            result = self.children[eachkey].suffixes()
                
            for eachres in result:
                return_res.append(eachkey + eachres)
    
        return return_res

        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
        node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[78]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def test(testcase):
    prefixNode = MyTrie.find(testcase[0])
    suff = []
    if prefixNode:
        suff = prefixNode.suffixes()

    print("Pass" if suff == testcase[1] else "Fail")

test(["a", ["nt", "nthology", "ntagonist", "ntonym"]])
test(["f", ["un", "unction", "actory"]])
test(["fa", ["ctory"]])
test(["trie", [""]])
test(["tie", []])