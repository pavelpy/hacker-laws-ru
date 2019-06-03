"""
Simple module for get links dict from md file.

"""

import re

from tools.config import PATH_TO_HACKER_LAWS_README_MD
from tools.simple_md_parser import MARKUP_REGEX


def get_links_dict():
    links_dict = {}
    with open(PATH_TO_HACKER_LAWS_README_MD, 'r') as original_file:
        original_file_content = original_file.read()

        for name, link in re.findall(MARKUP_REGEX, original_file_content):
            if name in links_dict:
                if link != links_dict[name]:
                    print('conflict', name, links_dict[name], link)
            else:
                links_dict[name] = link
    return links_dict


if __name__ == '__main__':
    print(get_links_dict()['Open a Pull Request'])
