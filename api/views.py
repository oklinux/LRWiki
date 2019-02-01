from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Doc
from .serializers import Docserializers
# Create your views here.


class DocView(APIView):

    def get(self, request):
        Docs=Doc.objects.all()
        serializers = Docserializers(Docs, many=True)
        response=[]
        for x in serializers.data:
            x.pop('text')
            response.append(x)
        print(response)
        return Response(response)
