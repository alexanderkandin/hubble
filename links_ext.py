import urllib.parse
import os


def get_links_ext(url):
    decode_url = urllib.parse.unquote(
        url)
    url = urllib.parse.urlparse(decode_url).path
    _, ext = os.path.splitext(url)
    return ext