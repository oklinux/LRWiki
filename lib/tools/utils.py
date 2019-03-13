import random
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth import get_user_model
import json
from lib.doc.create import create_doc
from lib.tools.payload_generator import generate_doc_data


def create_random_doc(author=None):
    """
    create a random doc by author
    """
    data = {'author': author}
    doc_data = generate_doc_data(**data)
    doc = create_doc(**doc_data)
    return doc


def random_user():
    """
    return a random user
    """
    User = get_user_model()
    all_user = User.objects.all()
    num = random.randint(0, len(all_user))
    return all_user[num]


class RandomUser:
    def __init__(self):
        self.user = random_user()
        self.account = self.user.account

    @property
    def client(self):
        client = APIClient(enforce_csrf_checks=False)
        client.force_authenticate(user=self.user)
        return client


class BaseTestCase(APITestCase):
    def setUp(self):
        self.users = {
            'Ua': RandomUser(),
            'Ub': RandomUser(),
        }
        self.docs = [create_random_doc(author=self.users[user].account) for user in self.users]


def get_title(text):
    title = text[text.find('#')+1:text.find('\n')]
    return title
