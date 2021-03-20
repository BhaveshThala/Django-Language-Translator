import io
from django.http import response
from django.http.response import HttpResponse
from googletrans import LANGUAGES,Translator
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import json


def dash(request):
    source=list(LANGUAGES.values())
    translator=Translator()


    if(request.method=='POST'):
        data=request.POST.get('source')
        fsrc=request.POST.get('options')
        fdest=request.POST.get('desti')

        # if(len(fsrc)<1):
        #     fsrc='hindi'

        if(len(data)<1):
            fl=request.FILES['document']
            content=fl.read()
            record=translator.translate(content,dest=fdest)
            return render(request,'index.html',{'src':source,'data':record.text})
        else:
            record=translator.translate(text=data,src=fsrc,dest=fdest)
            return render(request,'index.html',{'src':source,'data':record.text})
    else:
        return render(request,'index.html',{'src':source})

@csrf_exempt
def react(request):
    if(request.method=='POST'):
        body=request.body
        data=io.BytesIO(body)
        jdata=JSONParser().parse(data)
        translator=Translator()
        record=translator.translate(text=jdata['text'],src=jdata['src'],dest=jdata['dest'])
        return HttpResponse(record.text)
@csrf_exempt
def reactDrop(request):
    if(request.method=='GET'):
        source=list(LANGUAGES.values())
        data={}
        data['store']=source
        return HttpResponse(json.dumps(source))