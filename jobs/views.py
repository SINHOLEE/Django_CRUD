from django.shortcuts import render, get_object_or_404,redirect
from .models import Job
from faker import Faker
from pprint import pprint
import requests
# Create your views here.
def index(request):
    return render(request,'jobs/index.html')

def past_job(request):
    base_URL = 'HTTP://api.giphy.com/v1/gifs/search?'
    API_KEY = 'qzjmCqziEAePYzP4HRJmGnXD0LGTNIAC'
    fake = Faker('ko_KR')
    if request.method == 'POST':
        name = request.POST.get('name')
        jobs_ob = Job.objects.filter(name=name)
        if not jobs_ob:
            job_obj = Job()
            job_obj.name = name
            job_obj.past_job = fake.job()
            job_obj.save()


           
        else:
            job_obj = get_object_or_404(Job, name=name)
        q = job_obj.past_job.split()[0]

        data = requests.get(f'{base_URL}api_key={API_KEY}&q={q}&limit=1').json()
        pprint(data['data'][0]['images']['480w_still']['url'])
        context = {
            'job' : job_obj,
            'image_url' : data['data'][0]['images']['480w_still']['url']
        }
        
        
        return render(request, 'jobs/past_job.html', context)
    else:
   
        return redirect('jobs:index')