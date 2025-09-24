from django.shortcuts import redirect,render
from django.http import HttpResponse
import json

def home(request):
    a={'name':'vaibhav','age':22}
    data=json.dumps(a)
    parse=json.loads(data)
    return HttpResponse(f'<h1> Hii DRF and this is some content <br> {data} <br> {parse}</h1>')