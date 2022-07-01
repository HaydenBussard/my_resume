import requests
from webbrowser import get
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Job, Header, Work, School, Me, Work_Head, School_Head, Me_Head


def home(request):
    headers = Header.objects
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs, 'headers':headers})

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job':job_detail})

def career(request):
    career_detail = Work.objects
    return render(request, 'jobs/career.html', {'career':career_detail})

def education(request):
    school_detail = School.objects
    return render(request, 'jobs/education.html', {'school':school_detail})

def mylife(request):
    me_detail = Me.objects
    return render(request, 'jobs/mylife.html', {'me':me_detail})

def career_head(request):
    career_head_detail = Work_Head.objects
    return render(request, 'jobs/career.html', {'career_head':career_head_detail})

def education_head(request):
    school_head_detail = School_Head.objects
    return render(request, 'jobs/education.html', {'school_head':school_head_detail})

def mylife_head(request):
    me_head_detail = Me_Head.objects
    return render(request, 'jobs/mylife.html', {'me_head':me_head_detail})

# def index(request):
#     jobs = Job.objects
#     return render(request, 'index.html', {'index':index})

def index(request):
    r = requests.get('https://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')