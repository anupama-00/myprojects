from lib2to3.fixes.fix_input import context

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect


from company.models import Jobpost

from employee.models import Jobapply

from employee.models import SavedJob


# Create your views here.

def intro(request):
    return render(request,'intropage.html')

@login_required
def home(request):
    j=Jobpost.objects.all()
    context={'job':j}
    return render(request,'home.html',context)

@login_required
def applyjob(request,pk):
    u = request.user
    japply = Jobpost.objects.get(id=pk)
    if request.method=="POST":
        res=request.FILES.get('r')
        ctc=request.POST['c']
        ectc=request.POST['e']
        int=request.POST['i']
        a=Jobapply.objects.create(user=u,job=japply,resume=res,current_CTC=ctc,expected_CTC=ectc,interview_date=int)
        a.save()
        return redirect('employee:success')
    return render(request,'applyjob.html',{'japply':japply})

@login_required
def myjobs(request):
    user = request.user
    applied_jobs = Jobapply.objects.filter(user=user)
    context = {'applied_jobs': applied_jobs}
    return render(request, 'myjobs.html', context)

# def saved_jobs(request):
#     user=request.user
#     saved_jobs=Jobpost.objects.filter(user=user)
#     context={'saved':saved_jobs}
#     return render(request,'saved_jobs.html',context)

@login_required
def save_job(request,pk):
    jobsave =Jobpost.objects.get(id=pk)
    saved_job, created = SavedJob.objects.get_or_create(user=request.user, job=jobsave)

    if not created:
        pass
    return redirect('employee:saved_jobs')
@login_required
def saved_jobs(request):
    saved_jobs = SavedJob.objects.filter(user=request.user)
    return render(request, 'saved_jobs.html', {'saved_jobs': saved_jobs})

@login_required
def success(request):
    return render(request,'success_applied.html')


@login_required
def search(request):
    if request.method=="POST":
        query=request.POST['q']
        query1=request.POST['ql']
        if query or query1:
            b=Jobpost.objects.filter(Q(title__icontains=query) & Q(region__icontains=query1))

            return render(request,'search.html',{'jobsearch':b})
        return render(request, 'search.html')

def remove(request, pk):
    saved_job = SavedJob.objects.get(id=pk, user=request.user)
    saved_job.delete()
    return redirect('employee:saved_jobs')



