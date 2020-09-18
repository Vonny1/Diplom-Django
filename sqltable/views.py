from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from sqltable.models import WorkerResponse, WorkerfullinfoResponse, jsontext



def index(request):
      return HttpResponse(WorkerResponse)
def workertable(request):
      return  HttpResponse(WorkerResponse)
def workerfullinfotable(request):
      return HttpResponse(WorkerfullinfoResponse)

def jsonmaslo(request):
      return HttpResponse(jsontext)

