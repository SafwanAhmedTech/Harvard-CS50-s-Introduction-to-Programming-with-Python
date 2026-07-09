import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'^.+src="(https?://(?:www\.)?youtube.com/embed/[^"]+)".+$', s):
        url = match.group(1)
        if 'www.' in url:
            url = url.replace('www.', '')
        url = url.replace('youtube', 'youtu.be')
        url = url.replace('.com', '')
        url = url.replace('embed/', '')
        if 'https' not in url:
            url = url.replace('http', 'https')
        return url

    else:
        return None


...


if __name__ == "__main__":
    main()
