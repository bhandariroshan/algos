# Trie --> find
To check if a word exists or not, we have to start from the root of the Trie and then keep looking for every character until we hit the exact leaf. So if the word in n character long then the overall time complexity of this part would be O(n). 

There is only one varable called node required to keep track of the node while traversing in the Trie data structure, so the space complexity of this code would be O(1).

# Trie --> insert
Lets say we have m words that we need to insert and each word has a length of n. Then for each word we go character by character and check if the character exists in the Trie children dict. If the element does not exist, we insert to the dictionary and create a new trie node and attach it as value. Once another character comes, for the same word comes, we insert into that children and repeat the process. So everytime we insert a word of n length we have to reach the leaf of the Trie. So the overall time complexity of inserting one word would be O(n), whereas inserting m words would be O(mn).

Since there is only one variable called node used to keep track of the root while inserting, the space complexity of this part of the code is O(1).

# TrieNode --> Suffices
Lets say there are m words each of length n. Lets say, we searched for a prefix and all of the words stored in Trie start from the same prefix. As such it would reuire us to keep looking all the keys and thir childrens recursively. In total we would do m * n recursion to find the suffices. So overall time complexity of the code would be O(mn). 

In every call of suffices, we would be storing the results in an array. Atmost we would beed to store, m words of n length each. As such, overall space complexity of the code would be O(mn).