from django.test import TestCase
import json
from rest_framework import status
from lib.tools.utils import BaseTestCase
# Create your tests here.


class DocApiViewTestCase(BaseTestCase):
    def setUp(self):
        super(DocApiViewTestCase,self).setUp()
        self.url = '/api/doc/'

    def test_get_doc_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        docs = json.loads(response.content)
        self.assertEqual(len(docs), len(self.docs))


