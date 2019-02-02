import string
import random

CHARS = (
    string.ascii_uppercase + string.ascii_lowercase + string.digits
)


def random_string(length=10, chars=CHARS):
    """
    Generate a random alphanumeric string of the specified length.
    """
    return str(''.join(random.choice(chars) for _ in range(length)))


def generate_doc_data(**data):
    """
    Generate a random doc data.
    """
    doc_data = {
        'title': data.get('title', random_string()),
        'text': data.get('text', random_string()),
        'author': data.get('author', random_string())
    }
    return doc_data
