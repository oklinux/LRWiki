from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT
)
from .models import Doc
from .serializers import DocSerializers
from .permissions import IsAccountOrReadOnly
from lib.doc.query import get_doc_by_id
from lib.tools.utils import get_title
# Create your views here.


class DocView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request):
        """
        return all docs(title,account,data_time,update_time)
        """
        Docs = Doc.objects.all()
        serializers = DocSerializers(Docs, many=True)
        response = []
        for x in serializers.data:
            x.pop('text')
            response.append(x)
        return Response(response, status=HTTP_200_OK)

    def post(self, request):
        data = request.data.copy()
        data['author'] = str(request.user)
        data['title'] = get_title(request.user['text'])
        serializers = DocSerializers(data=data)
        if not serializers.is_valid(raise_exception=True):
            return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)
        new_data = {
            'title': serializers.validated_data['title'],
            'author': serializers.validated_data['author'],
        }
        serializers.save()
        return Response(new_data, status=HTTP_200_OK)


class DocDetailView(APIView):
    permission_classes = (IsAccountOrReadOnly,)

    def get_object(self, doc_id):
        doc = get_doc_by_id(doc_id)
        if not doc:
            raise Http404
        self.check_object_permissions(self.request, doc)
        return doc

    def get(self, request, doc_id):
        doc = self.get_object(doc_id)
        serializer = DocSerializers(doc)
        return Response(serializer.data, status=HTTP_200_OK)

    def put(self, request, doc_id):
        doc = self.get_object(doc_id)
        data = request.data.copy()
        data['title'] = get_title(data['text'])
        serializer = DocSerializers(doc, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
        data = serializer.validated_data
        serializer.save()
        return Response(data, status=HTTP_200_OK)

    def delete(self, request, doc_id):
        doc = self.get_object(doc_id)
        doc.delete()
        return Response(status=HTTP_204_NO_CONTENT)
