import requests
from webbrowser import get
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Job, Header


def home(request):
    headers = Header.objects
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs, 'headers':headers})

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job':job_detail})

# def index(request):
#     jobs = Job.objects
#     return render(request, 'index.html', {'index':index})

def index(request):
    r = requests.get('https://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')