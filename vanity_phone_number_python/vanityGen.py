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


class NumberError(Exception):
    """Raised if the 10-digit phone number does not have a corresponding 10-letter English word"""

    def __init__(self, message):
        self.__message = message

    message = property(lambda self: self.__message)

    def __str__(self):
        return str(self.message)


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
        if self.results:
            return self.results
        else:
            raise NumberError(
                "Oops! The phone number {} does not have a corresponding 10-letter English word.".format(
                    self.number
                )
            )
