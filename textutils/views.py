# I have Created this file - Sanskar
from django.http import HttpResponse
from django.shortcuts import render


# def index(response):
#     return HttpResponse(
#         '''<h1>Here are some helpful links for WEB-D</h1><a href ="https://stackoverflow.com/questions/23439089/using-django-admin-on-windows-powershell">How to start new Django Project</a>
#         <br> <a href ="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django playlist</a>
#        <br> <a href="https://getbootstrap.com/docs/5.2/getting-started/introduction/">Bootstrap</a>''')
#
#
# def about(response):
#     return HttpResponse("Welcome to textutils")
#
#
# def gymrules(response):
#     file = open('textutils/text.txt', 'r')
#     data = file.read()
#     return HttpResponse(data)

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")


def analyze(request):
    # get the text
    djangotext = request.POST.get('text', 'default')
    # checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    # check which check box is on
    if removepunc == "on":
        punctuations = '''!()-[];:'""\,<>.?/@#$%^&*_~'''
        analyzed = ""
        for char in djangotext:
            if char not in punctuations:
                analyzed += char
        djangotext = analyzed
        # Analyze the text
        params = {'purpose': 'Remove Punctuation', 'analyzedtext': analyzed}

    if fullcaps == "on":
        analyzed = ""
        for char in djangotext:
            analyzed = analyzed + char.upper()
        djangotext = analyzed
        params = {'purpose': 'Change all to UPPERCASE', 'analyzedtext': analyzed}

    if newlineremover == "on":
        analyzed = ""
        for char in djangotext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Line', 'analyzedtext': analyzed}

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on":
        return HttpResponse("ERROR")
    return render(request, 'analyze.html', (params))
