
class Trie(object):

    def __init__(self):
        self.curr_node = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.curr_node
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["#"] = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.curr_node
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return node["#"]


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.curr_node
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)