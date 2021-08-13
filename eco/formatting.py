import re


def discord_friendly_message(input: str) -> str:
    """ Convert eco messages into discord friendly message"""
    strip_tag_pattern = re.compile('</?[^>]+>')
    return strip_tag_pattern.sub('', input.replace('<br>', '\n'))
