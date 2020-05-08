#from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from uploadapp import serializers
from .serializers import HelloSerializer
import requests
import time
import os
from .reco import *



class FileUploadView(APIView):
    #parser_class = (FileUploadParser,)
    
    def post(self, request, *args, **kwargs):
        
        url_serializer = HelloSerializer(data=request.data)
        serializer_class = serializers.HelloSerializer
        serializer =HelloSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.validated_data.get('obj')
            rec_items=recom.recommendation_for_user(obj)
            print(rec_items)
            return Response(rec_items, status=status.HTTP_201_CREATED)


