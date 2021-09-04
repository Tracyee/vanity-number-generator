from lexicon import Lexicon
from typing import List

digit2letter: List[str] = [
    "",
    "",
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz",
]


class VanityGen:
    def __init__(self, number: str, lexicon: Lexicon):
        self.number = number
        self.lexicon = lexicon
        self.results: List[str] = []

    def vanityRec(self, prefix: str, depth: int):
        if depth == 10:
            if self.lexicon.containsWord(prefix):
                self.results.append(prefix)
            return
        for letter in digit2letter[int(self.number[depth])]:
            if self.lexicon.containsPrefix(prefix + letter):
                self.vanityRec(prefix + letter, depth + 1)

    def getMyVanity(self) -> List[str]:
        self.vanityRec("", 0)
        return self.results
