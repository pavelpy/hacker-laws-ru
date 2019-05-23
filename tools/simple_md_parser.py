"""
    Parser for original README.md file.
"""

import re

# Anything that isn't a square closing bracket
NAME_REGEX = "[^]]+"
LINK_REGEX = "[^)]+"

MARKUP_REGEX = '\[({0})]\(\s*({1})\s*\)'.format(NAME_REGEX, LINK_REGEX)


def main():
    with open('../hacker-laws/README.md') as f:
        for line in (l.strip() for l in f if l.strip()):
            line = line.lstrip('# *->')
            line_text = line

            # Remove links.
            for match in re.findall(MARKUP_REGEX, line_text):
                line = line.replace('[{0}]({1})'.format(*match), '[{0}]'.format(*match))
            print(line)


if __name__ == '__main__':
    main()
