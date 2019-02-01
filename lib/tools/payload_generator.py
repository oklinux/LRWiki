import string
import random
from django.utils import timezone

CHARS = (
    string.ascii_uppercase + string.ascii_lowercase + string.digits
)


def random_string(length=10, chars=CHARS):
    """
    Generate a random alphanumeric string of the specified length.
    """
    return str(''.join(random.choice(chars) for _ in range(length)))


def generate_doc_data(**data):
    doc_data = {
        'title': data.get('title', random_string()),
        'text': data.get('text',random_string()),
        'title': data.get('title',random_string()),
    }
    return doc_data
