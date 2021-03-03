# File: extract_sents.py
# Author: Taede Meijer
# Date: 2/28/2021
# Description: extract tokenized sentences from idiosyncratic text files

import re
import gzip
import sys


def solve_punctuation(text):
    ''' Finish tokenization by adding spaces before and/or after punctuation'''

    finaltext = ""

    for line in text:

        # Because of the way I .join the text there's some double spaces.
        processedline = re.sub('  ', ' ', line)

        final_line = ""

        # By storing the punctuation that are always directly behind a word
        # we can easily add more punctuation to the program
        punctuationafter = ",:.!)?"

        # Same goes for punctuation that comes strictly before a word.
        punctuationbefore = "("

        # There's also punctuation that can be both in front of and behind
        # a word.
        punctuationboth = "\'\""

        for i in range(len(processedline)):

            # Store the current character for efficiency purposes.
            current_char = processedline[i]

            if current_char in punctuationbefore:
                final_line += current_char + ' '

            elif current_char in punctuationafter:
                final_line += ' ' + current_char

            elif current_char in punctuationboth:

                if i == 0:
                    final_line += current_char + ' '

                elif i == len(processedline) - 1:
                    final_line += ' ' + current_char

                elif processedline[i-1] == ' ':
                    final_line += current_char + ' '

                elif (processedline[i+1] == ' ' or
                        processedline[i+1] in punctuationafter):
                    final_line += ' ' + current_char

                # This exception handles words like thema's and foto's
                elif current_char == '\'':
                    final_line += current_char

            else:
                final_line += current_char

        finaltext += final_line + '\n'

    return finaltext


def main(argv):

    with gzip.open(argv[1], 'rt', encoding='utf8') as inp:
        content = inp.read()

        content = content.splitlines()
        body = ' '.join(content[4:-7])

        regex = re.compile(r'([\"\']?[A-Z][^\.!?]*[\.!?][\"\']?)', re.M)

        print(solve_punctuation(regex.findall(body)))

    quit()


if __name__ == "__main__":
    main(sys.argv)
