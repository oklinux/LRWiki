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

    def test_get_doc_detail(self):
        """
        get doc detail,it will success and return doc detail
        :return:
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_doc(self):
        """
        put Ua url random data , it will success and return status 200
        """
        data = generate_doc_data()
        response = self.users['Ua'].client.put(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_doc(self):
        """
        delete Ua's doc it will success and return 204
        """
        response = self.users['Ua'].client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
