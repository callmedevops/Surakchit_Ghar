from django.shortcuts import render, HttpResponse
def index(request):
    return render(request,'ku/project/pages/room2.html')