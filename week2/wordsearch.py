# File: wordsearch.py
# Author: Taede Meijer
# Date: 2/15/2021
# Description: Program that solves a wordsearch puzzle. It takes a .txt puzzle
# and a list of words .json as input. Option for advanced search

import argparse
import json


def check_horizontal(rows, word):
    ''' Function that returns true if the word is found in one of the rows
    of the puzzle. '''
    for row in rows:
        if word in row:
            return True

    return False


def check_vertical(columns, word):
    ''' Function that returns true if the word is found in one of the columns
    of the puzzle '''
    for column in columns:
        if word in column:
            return True
    return False


def solve(puzzletxt, wordsjson, advanced=False):
    # Open the txt file, store the rows of the puzzle
    infile = open(puzzletxt, 'r')
    rows = infile.read().splitlines()

    # Close the infile, we no longer need it
    infile.close()

    # Make a string to safe the letters from top to bottom, left to right.
    columns = ""

    # I use two different length variables, for if the rows are not the same
    # length as the columns
    for i in range(len(rows[0])):
        for j in range(len(rows)):
            columns += rows[j][i]

    # Split the string every n characters (where n is the length of a column),
    # so there are no false positives which would go from the bottom of one
    # column to the top of the next
    n = len(rows)
    columns = [(columns[i:i+n]) for i in range(0, len(columns), n)]

    # Advanced word search
    if advanced == "True":
        advanced = True
        reversed_rows = []
        reversed_columns = []

        # Reverse the rows and columns, these are two different loops, for if
        # the search is not a perfect square
        for i in range(len(rows)):
            reversed_rows.append(rows[i][::-1])

        for i in range(len(columns)):
            reversed_columns.append(columns[i][::-1])

    # Open the json file
    with open(wordsjson) as data_file:
        data = json.load(data_file)

    # Iterate through every word of the json and look for it in the rows.
    words_found = set()
    for word in data['words']:
        word = word.upper()
        if check_horizontal(rows, word) is True:
            words_found.add(word)

        if advanced:
            if check_horizontal(reversed_rows, word) is True:
                words_found.add(word)

        if check_vertical(columns, word) is True:
            words_found.add(word)

        if advanced:
            if check_horizontal(reversed_columns, word) is True:
                words_found.add(word)

    return words_found


def main():
    # argparse
    parser = argparse.ArgumentParser(description='Wordsearch puzzle')
    parser.add_argument('puzzlefile', type=str,
                        help='Filepath for the txt file of the puzzle')
    parser.add_argument('wordlist', type=str,
                        help='Filepath for the json file of the wordlist')
    parser.add_argument('advanced', type=str,
                        nargs='?', const="False",
                        help='Add "True" if you want to run advanced version')

    args = parser.parse_args()

    # Run the program
    print(solve(args.puzzlefile, args.wordlist, args.advanced))


if __name__ == "__main__":
    main()
