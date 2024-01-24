class TrieNode:
  def __init__(self):
    self.children={}
    self.is_end_of_word=False

def insert_word(root,word):
  node=root
  for char in word:
    if char not in node.children:
      node.children[char]=TrieNode()
    node=node.children[char]

  node.is_end_word=True
      