from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# only GET
"""@api_view(['GET'])
def home(request):
    if request.method=='GET':
        return Response({'msg':'Welcome get'})"""

# put
"""@api_view(['PUT'])
def home(req):
    return Response({'msg':'PUT MEthod is called'})"""
    
# both GET & POST
@api_view(['POST','GET','PUT','DELETE'])
def home(request):    
    if request.method=='GET':
        print(request.data)
        return Response({'msg':'Welcome get'})
    
    if request.method=='POST':
        print(request.data)
        return Response({'msg':'Welcome POST!!!!!!','data':request.data})

    
    if request.method=='PUT':
        print(request.data)
        return Response({'msg':'Welcome PUT is called in one fuction'})

    
    if request.method=='DELETE':
        print(request.data)
        return Response({'msg':'Welcome DELETE!'})


    return Response('OUTOFF MEthod something Called')
