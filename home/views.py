from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb

def server(request):
        return render(request, 'home/servers.html')
def index(request):
        return render(request, 'home/home.html')
def nf(request):
        return render(request, 'home/nf.html')
