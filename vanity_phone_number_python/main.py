from lexicon import Lexicon
from vanityGen import VanityGen


def main():
    # read from an English word file to a lexicon tree
    lexicon = Lexicon()
    with open("wiki-100k.txt", "r") as f:
        lines = [line.rstrip() for line in f]
        for word in lines:
            lexicon.add(word)

    phoneNumber = 2222222222
    while True:
        phoneNumber = input("Enter a phone number: ")
        vanityGen = VanityGen(phoneNumber, lexicon)
        vanities = vanityGen.getMyVanity()
        print("phone number: {}, vanity: ".format(phoneNumber), end="")
        for vanity in vanities:
            print("{} ".format(vanity), end=" ")
        print("")


if __name__ == "__main__":
    main()
