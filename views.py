from django.shortcuts import render

def index(request):
  return render(request, 'articles/list.html')

def content(request):
  return render(request, 'contents/testcont.html')