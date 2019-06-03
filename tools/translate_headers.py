import string

from tools.config import PATH_TO_HACKER_LAWS_README_MD

ALLOWED_CHARACTERS = string.digits + ' ' + string.ascii_lowercase


def get_markdown_anchor(header):
    header = header.lower().lstrip('# ')
    header = ''.join(c for c in header if c in ALLOWED_CHARACTERS)
    header = header.replace(' ', '-')
    return header


def replace_headers(file_content):
    sorted_header_replace_list = sorted(get_header_replace_list(),
                                        key=lambda x: len(x[0]), reverse=True)
    for header, replacement in sorted_header_replace_list:
        file_content = file_content.replace(header, replacement)

    return file_content


def get_header_replace_list():
    result = []
    with open(PATH_TO_HACKER_LAWS_README_MD, 'r') as f:
        for line in (l.strip() for l in f if l.strip()):
            if line.startswith('#'):
                anchor = get_markdown_anchor(line)
                title = line.lstrip('# ')
                header_level = line.replace(title, '').strip()
                replace_header = '{header_level} <a name="{anchor}"></a>{title}'.format(**locals())
                result.append((line, replace_header))
    return result


if __name__ == '__main__':
    for item in get_header_replace_list():
        print(item)
