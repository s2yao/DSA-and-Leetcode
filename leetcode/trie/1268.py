'''
We created a Trie
Where each node carries a suggestion, from the root all the way to the current node's top 3 suggestion
In the future when using Trie, always think about what else would each node carry as a parameter
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestion = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
            if len(curr_node.suggestion) < 3:
                curr_node.suggestion.append(word)

    def get_suggestions(self, prefix):
        curr_node = self.root
        ret = []
        for suggestion_char in prefix:
            if suggestion_char not in curr_node.children:
                while len(ret) < len(prefix):
                    ret.append([])
                return ret
            curr_node = curr_node.children[suggestion_char]
            ret.append(curr_node.suggestion)
        return ret

class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        trie = Trie()
        for product in products:
            trie.insert(product)
        return get_suggestions(searchWord)

products = ['mobile', 'moneypot', 'monitor', 'mouse', 'mousepad']
products.sort()
print(products)