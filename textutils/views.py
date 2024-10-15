# My file --- shreyansh
import string
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    prams = {"golu": "bhum","sh":"gh"}
    return render(request,'index.html',prams)

def hello(request):
    return HttpResponse("gyg")

def removepunc(request):
    #get the text from request
    djtext = request.POST.get('text','default')
    flag = request.POST.get("puctuation","off")
    count_flag = request.POST.get("count","off")
    upper = request.POST.get("upper_case","off")
    if flag == "on":

        ans = ""
        punct = string.punctuation
        for ele in djtext:
            if ele not in punct:
                ans+= ele
        print(type(punct))


        param = {"input":djtext,"result": ans,"work": "removing the puctuation :"}


        return render(request,'analyse.html',param)
    elif(count_flag == "on"):

        param = {"input": djtext, "result": len(djtext),"work": "no of character is :"}
        return render(request,'analyse.html',param)

    elif upper == "on":
        param = {"input":djtext,"result":djtext.upper(),"work": "uppercase of input string is :"}
        return render(request, 'analyse.html', param)

    else:
        return HttpResponse("someting missing which you are not fill ; ERROR <br> <a href = 'http://127.0.0.1:8000/'>go back</a> ")
