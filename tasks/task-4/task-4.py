"""
Shortest unique prefix

Given a list of words, for each word find the shortest unique prefix. You can assume a word will
not be a substring of another word (ie play and playing won't be in the same words list)

Example
Input: ['joma', 'john', 'jack', 'techlead']
Output: ['jom', 'joh', 'ja', 't']
"""

class Node:
    def __init__(self):
        
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for char in word: 
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
            current.count += 1


    def find_prefix(self,word):
        current = self.root
        prefix = ""

        for char in word:  
            if current.count==1:
                return prefix
            else:
                prefix += char
                current = current.children[char]
        return prefix


def shortest_unique_prefix(words):
    # Fill this in.
    trie = Trie()

    for word in words:
        trie.insert(word)

    result = []
    for word in words:
        result.append(trie.find_prefix(word))

    return result


print(shortest_unique_prefix(['joma', 'john', 'jack', 'techlead']))
    
        