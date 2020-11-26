
from django.http import HttpResponse
from django.shortcuts import render
import operator
# def homepage(request):
#     return HttpResponse("<h1>India is the best</h1>")

# def homepage(request):
#     return render(request,"home.html",{"name":"akshay"})

def homepage(request):
    return render(request,"home.html")

def count(request):
    data=request.GET["fulltextarea"]
    word_list=data.split()
    list_length=len(word_list)

    word_dict={}
    for word in word_list:
        if word[-1::]==".":
                w1=word.split(".")
                w1.pop()
                str1=""
                str1 +=w1[0]
                word=str1
        
        if word[-1::]==",":
                w2=word.split(",")
                w2.pop()
                str2=""
                str2 +=w2[0]
                word=str2

        if word in word_dict:
            word_dict[word] +=1 
        
        else:
            word_dict[word] = 1

    sorted_list=sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,"count.html",{"text" : data,"words" : list_length,"lst" : word_list,"dict_item" : sorted_list})

def about(request):
    return render(request,"about.html")

# def contact(request):
#     return HttpResponse("<h1>contact us</h1><br>This is your contact working page")