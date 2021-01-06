#!/usr/bin/env python3

# Generate tex file for a random bingo card from a word list

import math
import random
import string


def main(taglist='taglist',
         tex_output='bingo.tex',
         tex_template='bingo_template.tex',
         size=5,
         bingo_center=True,
         bingo_string='BINGO'):
    """
    Build tex-file for bingo card.

    Parameters
    ----------
    taglist: str
        path to text file with list of words
    tex_output: str
        path to tex file that should be produced
    tex_template: str
        path to tex template from which output file is built
    size: int
        number of rows/columns in bingo card;
        for example, size=4 yields a card with 4*4=16 fields
    bingo_center: bool
        should the middle field be a BINGO! wildcard?
    bingo_string:
        what string should be used for the wildcard field?
    """
    # construct bingo card as dict
    card = bingodict(filename=taglist,
                     size=5,
                     bingo_center=True,
                     bingo_string='BINGO!')
    # convert dict to string for tikz matrix
    matrix = texmatrix(card=card, size=size)
    # insert matrix into template...
    with open(tex_template, "r") as template:
        tex = template.read()
        tex = tex.replace("{{{MATRIX}}}", matrix)
    # ...and write to specified output file
    with open(tex_output, "w") as output:
        output.write(tex)


def bingodict(
        filename='taglist',
        size=5,
        bingo_center=True,
        bingo_string='BINGO!'):
    """Construct size*size bingo card dict from wordlist."""
    # cards with even size cannot have a BINGO! field in the middle
    if size % 2 == 0:
        bingo_center = False

    # load random tags
    fields = size**2 - bingo_center
    tags = randpick(filename=filename, fields=fields)

    # build dictionary of coordinates
    coords = {(x, y): None
              for x in range(1, size+1)
              for y in range(1, size+1)}

    # set value of center field;
    # never matters for cards with even number of columns/rows
    if size % 2 == 1:
        if not bingo_center:
            bingo_string = tags.pop()
        center = math.ceil(size/2)
        coords[(center, center)] = bingo_string

    # fill remaining fields that have no entry
    for key, val in coords.items():
        if not val:
            coords[key] = tags.pop()

    # add row and column labels
    for coord in range(1, size+1):
        # number for row
        coords[(coord, 0)] = coord
        # letter for columns
        coords[(0, coord)] = string.ascii_uppercase[coord - 1]
        # top left corner is empty
        coords[(0, 0)] = ""

    return coords


def load_wordlist(filename='taglist'):
    """Load all allowed field entries from file."""
    with open(filename, 'r') as taglist:
        return taglist.read().splitlines()


def randpick(filename='taglist', fields=0):
    """Randomly pick fixed number of field entries."""
    tags = load_wordlist(filename=filename)
    if len(tags) < fields:
        raise ValueError(f"Taglist contains less than {fields} entries")
    return random.sample(tags, fields)


def texmatrix(card={}, size=5):
    """Convert dict of bingo card to string for tikz matrix."""
    matrix = ""
    for row in range(size+1):
        for col in range(size+1):
            val = card[(row, col)]
            matrix += format_cell(row=row, col=col, val=val, size=5)
    return matrix


def format_cell(row=0, col=0, val="", size=5):
    """Convert each dict entry to a tikz matrix cell."""
    separator = "\\\\\n" if col == size else "& "
    if row == 0 and col == 0:
        style = "top-left"
    elif row == 0:
        style = "row-label"
    elif col == 0:
        style = "col-label"
    elif (row + col) % 2 == 0:
        style = "dark"
    else:
        style = "light"
    # ugly hack because tikz fails to rotate text indepenently of background
    angle = {"dark": "\\darkangle",
             "light": "\\lightangle",
             "col-label": "\\colangle",
             "row-label": "\\rowangle",
             "top-left": "0",
             }
    content = "\\rotatebox{" + angle[style] + "}{" + str(val) + "}"
    return f"|[{style}]| {content} {separator}"


if __name__ == "__main__":
    main()
