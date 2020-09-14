"""Change words into 'pig latin'."""
import sys


def main():
    """Get word or sentence from input and change every word into 'pig latin'."""
    print("Get word or sentence from input and change every word into 'pig latin'.\n")

    consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]

    while True:
        word_to_change = input("Give a word or sentence: (Leave blank to quit)\n")

        if word_to_change == "":
            break
        elif len(word_to_change) < 2:
            print("\n\nWord too short, let's try another one.\n\n", file=sys.stderr)
        else:
            suff = "ay" if (consonants.index(word_to_change[0].upper()) > -1) else "way"

            pig_latin_word = word_to_change[1:] + word_to_change[0] + suff

            print("\n")
            print("{}".format(pig_latin_word))
            print("\n")


if __name__ == '__main__':
    main()
