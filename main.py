import pandas as pd


def load_data(revert=False):
    morse_df = pd.read_csv("morse_dictionary.csv")

    if revert:
        converter = {row.code: row.letter for (i, row) in morse_df.iterrows()}
    else:
        converter = {row.letter: row.code for (index, row) in morse_df.iterrows()}

    return converter


def to_morse_converter():
    converter = load_data()
    user_word = input("Type down a word: \n").upper()

    try:
        morse_code = [converter[letter] for letter in user_word]
    except KeyError:
        print(f"Allowed characters: {converter.keys()}")
        to_morse_converter()
    else:
         for code in morse_code:
             print(code, end=' ', flush=True)


def to_text_converter():
    converter = load_data(revert=True)
    user_morse_word = input("Type down morse code: \n").strip()

    morse_letter_list = user_morse_word.split(" ")

    try:
        text = [converter[code] for code in morse_letter_list]
    except KeyError:
        print(f"Allowed characters: {converter.keys()}")
        to_text_converter()
    else:
        for l in text:
            print(l, end='', flush=True)


if __name__ == '__main__':
    # to_morse_converter()
    to_text_converter()
