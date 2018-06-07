from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb

def ref(request):
    query = request.GET.get('s')
    if query in "list.enjuu.click":
        context= {
            'server': query,
        }
        return render(request, 'home/redirect.html', context)
    else:
        return render(request, 'home/redirect.html')

def addserver(request):
        return render(request, 'home/addserver.html')
def add(request):
        return render(request, 'home/add.html')
def server(request):
        return render(request, 'home/servers.html')
def index(request):
        return render(request, 'home/home.html')
