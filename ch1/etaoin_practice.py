"""Count letters in a sentence and display results in a form of console bar chart."""
# import collections
import pprint
import string


def main():
    """Read a sentence, then count letters and put results into a dictionary."""
    print("Let's count letters in a given sentence.\n")

    while True:
        sentence = input("Give a sentence: (Leave blank and press ENTER to quit)\n")

        if sentence == "":
            break
        else:
            # sentence_letters = collections.defaultdict(list)
            # sentence_letters = collections.defaultdict(int)
            sentence_letters = dict((letter, []) for letter in string.ascii_lowercase)

            for char in sentence:
                if char.isalpha():
                    sentence_letters[char.lower()].append(char.lower())
                    # sentence_letters[char.lower()] += 1

            print("\n")
            pprint.pprint(sentence_letters, indent=6, width=180, sort_dicts=True)
            print("\n")


if __name__ == '__main__':
    main()
