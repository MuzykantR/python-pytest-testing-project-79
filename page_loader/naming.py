import re
from urllib.parse import urlparse


def generate_filename(url: str):
    """
    Генерирует имя файла из URL.

    Примеры:
        https://ru.hexlet.io/courses → ru-hexlet-io-courses.html
        https://example.com/blog/post → example-com-blog-post.html
    """

    parsed = urlparse(url)
    parts = parsed.netloc + parsed.path + "?" + parsed.query

    name = re.sub(r'[^a-zA-Z0-9]', '-', parts)
    name = re.sub(r'-+', '-', name)
    name = name.strip('-')

    if not name.endswith('.html'):
        name += '.html'

    return name
