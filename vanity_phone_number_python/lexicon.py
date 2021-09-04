from typing import Dict


class Node:
    def __init__(self):
        self.isWord = False
        self.suffixes: Dict[str, Node] = {}


class Lexicon:
    def __init__(self):
        self.root: Node = Node()

    def add(self, string: str):
        self.getNode(string).isWord = True

    def containsWord(self, string: str) -> bool:
        found = self.findNode(string)
        return found is not None and found.isWord

    def containsPrefix(self, string: str) -> bool:
        return self.findNode(string) is not None

    def getNode(self, string: str) -> Node:
        curr = self.root
        for pos in range(len(string)):
            try:
                curr = curr.suffixes[string[pos]]
            except KeyError:
                curr.suffixes[string[pos]] = Node()
                curr = curr.suffixes[string[pos]]
        return curr

    def findNode(self, string: str) -> Node:
        curr = self.root
        for pos in range(len(string)):
            curr = curr.suffixes[string[pos]] if string[pos] in curr.suffixes else None
            if curr is None:
                break

        return curr
