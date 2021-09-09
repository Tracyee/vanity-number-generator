from lexicon import Lexicon
from vanityGen import VanityGen, NumberError

letter2digit = {
    "a": 2,
    "b": 2,
    "c": 2,
    "d": 3,
    "e": 3,
    "f": 3,
    "g": 4,
    "h": 4,
    "i": 4,
    "j": 5,
    "k": 5,
    "l": 5,
    "m": 6,
    "n": 6,
    "o": 5,
    "p": 7,
    "q": 7,
    "r": 7,
    "s": 7,
    "t": 8,
    "u": 8,
    "v": 8,
    "w": 9,
    "x": 9,
    "y": 9,
    "z": 9,
}

from collections import defaultdict


def buildHashmap():
    mapping = defaultdict(list)
    with open("wiki-100k.txt", "r") as f:
        print("Loading word file...")
        lines = [line.rstrip() for line in f]
        print("Adding words to the lexicon tree...")
        for word in lines:
            if len(word) == 10:
                number: str = ""
                for letter in word:
                    number += str(letter2digit[letter])
                mapping[number].append(word)

    return mapping


def main():
    mapping = buildHashmap()
    while True:
        try:
            phoneNumber = input("Enter a phone number: ")
        except EOFError:
            print("\nProgram terminated!")
            exit(0)
        try:
            int(phoneNumber)
        except ValueError:
            print("Please enter a valid phone number!")
            continue

        vanities = mapping[phoneNumber]
        if vanities:
            print("phone number: {}, vanity: ".format(phoneNumber), end="")
            for vanity in sorted(vanities, reverse=True):
                print("{} ".format(vanity), end=" ")
            print("")
        else:
            print(
                "Oops! The phone number {} does not have a corresponding 10-letter English word.".format(
                    phoneNumber
                )
            )


if __name__ == "__main__":
    main()
