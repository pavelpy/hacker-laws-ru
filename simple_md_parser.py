"""
    Parser for original README.md file.
"""

import re

# Anything that isn't a square closing bracket
name_regex = "[^]]+"
# http:// or https:// followed by anything but a closing paren
link_regex = "[^)]+"

markup_regex = '\[({0})]\(\s*({1})\s*\)'.format(name_regex, link_regex)

with open('../hacker-laws/README.md') as f:
    for line in (l.strip() for l in f if l.strip()):
        line = line.lstrip('# *->')
        line_text = line
        for match in re.findall(markup_regex, line_text):
            line = line.replace('[{0}]({1})'.format(*match), '[{0}]'.format(*match))
        print(line)
