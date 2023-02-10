from django.http import HttpResponse
from django.shortcuts import render
import heapq
import os
def index(request):
    return render(request,'html\home.html')

def compress(request):
    return render(request,'html\compress.html')

def decompression(request):
    return render(request,'html\decompression.html')

    
    
