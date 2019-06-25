"""
    Parser for original README.md file.
"""

import re
import os
from collections import Counter
import gspread
from oauth2client.service_account import ServiceAccountCredentials as ServiceAC

# Anything that isn't a square closing bracket
NAME_REGEX = "[^]]+"
LINK_REGEX = "[^)]+"

MARKUP_REGEX = '\[({0})]\(\s*({1})\s*\)'.format(NAME_REGEX, LINK_REGEX)


def main():
    with open(os.path.abspath('../../hacker-laws/README.md')) as f:
        for line in (l.strip() for l in f if l.strip()):
            line = line.lstrip('# *->')
            line_text = line

            # Remove links.
            for match in re.findall(MARKUP_REGEX, line_text):
                line = line.replace('[{0}]({1})'.format(*match), '[{0}]'.format(*match))
            print(line)


def print_new_lines():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAC.from_json_keyfile_name('gspread.json', scope)

    gc = gspread.authorize(credentials)
    # Open a worksheet from spreadsheet with one shot
    worksheet = gc.open("hacker-laws-ru-readme.md").sheet1
    values_list = list(worksheet.col_values(1))
    counter = dict(Counter(values_list))

    with open(os.path.abspath('../../hacker-laws/README.md')) as f:
        for line in (l.strip() for l in f if l.strip()):
            line = line.lstrip('# *->')
            line_text = line

            # Remove links.
            for match in re.findall(MARKUP_REGEX, line_text):
                line = line.replace('[{0}]({1})'.format(*match), '[{0}]'.format(*match))
            if not counter.get(line):
                print(line)


if __name__ == '__main__':
    # main()
    print_new_lines()
