from django.test import TestCase
import json
from rest_framework import status
from lib.tools.utils import BaseTestCase
from lib.tools.payload_generator import generate_doc_data
# Create your tests here.


class DocApiViewTestCase(BaseTestCase):
    def setUp(self):
        super(DocApiViewTestCase, self).setUp()
        self.url = '/api/doc/'

    def test_get_doc_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        docs = json.loads(response.content)
        self.assertEqual(len(docs), len(self.docs))

    def test_post_doc_without_login(self):
        """
        Don't login then post new doc
        """
        data = generate_doc_data()
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_doc(self):
        data = generate_doc_data()
        response = self.users['Ua'].client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res_data = json.loads(response.content)
        self.assertEqual(res_data['title'], data['title'])


class DocDetailApiViewTestCase(BaseTestCase):
    def setUp(self):
        super(DocDetailApiViewTestCase,self).setUp()
        self.url = f'/api/doc/{self.docs[0].id}/'
        print(self.url)

    # def test_put_doc(self):
    #     data = generate_doc_data()
    #     response = self.users['Ua'].client.put(self.url, data=data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
