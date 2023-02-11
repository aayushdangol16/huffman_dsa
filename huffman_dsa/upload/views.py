from django.http import HttpResponse
from django.shortcuts import render
from .models import FilesUpload
from .import huffman
from .import decompress

def index(request):
    return render(request,'html\home.html')

def compress(request):
    if request.method=="POST":
        file2=request.FILES["file"]
        document=FilesUpload.objects.create(file=file2)
        document.save()
        fname=str(file2)
        output_path=huffman.hcompress(fname)
        with open(output_path,'rb') as q:
            data=q.read()
        response = HttpResponse(data, content_type='text/plain')
        response['Content-Disposition'] =f'attachment; filename="{output_path[6:]}"'
        q.close()
        return response
        
    return render(request,'html\compress.html')
    

def decompression(request):
    if request.method=="POST":
        file2=request.FILES["file"]
        document=FilesUpload.objects.create(file=file2)
        document.save()
        fname=str(file2)
        decom_path=decompress.hdecompress(fname)
        with open(decom_path,'r') as q:
            data=q.read()
        response = HttpResponse(data, content_type='text/plain')
        response['Content-Disposition'] =f'attachment; filename="{decom_path[6:]}"'
        q.close()
        return response
    return render(request,'html\decompression.html')

    
    
