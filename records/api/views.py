from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request

from app.models import File
from api.serializers import  FileSerializer,UserSerializer

from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.conf import settings

import json
import csv

# USER VIEW
class UserViewSet(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

#VIEW FILES
class FileList(viewsets.ModelViewSet):
    page_size = 5
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]

#DETAIL FILES
class Detail_File(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]
    
    #rewriting class read
    def retrieve(self, request, pk):
        instance = File.objects.get(pk=pk)
        data =[]

        #method to open csv file
        with open('{}/{}'.format(str(settings.MEDIA_ROOT),str(instance.file_data)), newline='') as datasheet:  
            reader = csv.DictReader(datasheet, delimiter=';', quotechar=';',
                        quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                data.append(row)
        
        #method to sort the csv file
        if 'order'  in request.query_params:
            order = request.query_params.get('order')
            data = sorted(data, key=lambda k: k[order].lower())       
        if 'order'  in request.query_params and 'desc' in request.query_params :
            desc = request.query_params.get('desc')
            order = request.query_params.get('order')
            if desc.lower() == 'true' :
                order_reverse = True
            else: 
                order_reverse = False
            data = sorted(data, key=lambda k: k[order].lower(), reverse=order_reverse) 
        
        
        #method to filter the csv file   
        if 'search' in request.query_params:
            search = request.query_params.get('search') 
            data = json.dumps(data)
            data = json.loads(data)
            data = [(x) for x in data for l in x.values() if l.lower() == search.lower()]
        
        if json.dumps(data):
            return Response(data, status=200)
        else:
            data = {'message': 'No se encontro el archivo'}
            return Response(data, status=200)
    
    