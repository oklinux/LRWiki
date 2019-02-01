from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Doc
from .serializers import DocSerializers

# Create your views here.


class DocView(APIView):
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
        print(response)
        return Response(response)
