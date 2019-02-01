from rest_framework.test import APIClient, APITestCase
import json
from lib.doc.create import create_doc
from lib.tools.payload_generator import generate_doc_data


def create_random_doc():
    data = generate_doc_data()
    doc = create_doc(**data)
    return doc


class BaseTestCase(APITestCase):
    def setUp(self):
        self.docs = [create_random_doc() for _ in range(3)]




