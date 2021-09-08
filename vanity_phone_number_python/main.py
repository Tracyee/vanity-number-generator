from lexicon import Lexicon
from vanityGen import VanityGen, NumberError


def main():
    # read from an English word file to a lexicon tree
    lexicon = Lexicon()
    with open("wiki-100k.txt", "r") as f:
        print("Loading word file...")
        lines = [line.rstrip() for line in f]
        print("Adding words to the lexicon tree...")
        for word in lines:
            lexicon.add(word)
        print("Complete!")

    phoneNumber = 2222222222
    while True:
        try:
            phoneNumber = input("Enter a phone number: ")
        except EOFError:
            print("\nProgram terminated!")
            exit(0)
        vanityGen = VanityGen(phoneNumber, lexicon)
        try:
            vanities = vanityGen.getMyVanity()
        except NumberError as e:
            print(e)
            continue
        print("phone number: {}, vanity: ".format(phoneNumber), end="")
        for vanity in vanities:
            print("{} ".format(vanity), end=" ")
        print("")


if __name__ == "__main__":
    main()
