# File: cdb.py
# Author: Taede Meijer
# Date: 2/15/2021
# Description: Returns a collection of adjectives in a database

import sys
import xml.etree.ElementTree as ET


def get_adjectives(filepath):

    tree = ET.parse(filepath)
    cdbid = tree.getroot()

    # I can't get the filtered list comprehension to work for the life of me :(
    # This works though :)
    collection = set()

    for cid in cdbid:
        # Get the form and pos of the current cid
        form = cid.attrib['form']
        pos = cid.attrib['pos']
        # If it matches the requirement, add it to the set.
        if pos == "ADJ":
            if form not in collection:
                collection.add(form)

    # Return the set
    return collection


def main():
    print(get_adjectives('cdb-sample.xml'))


if __name__ == "__main__":
    main()
