from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect

from company.models import Jobpost



# Create your views here.
@login_required
def jobpost(request):
    if request.method=="POST":
        img=request.FILES['f']
        email = request.POST['e']
        tit = request.POST['t']
        loc = request.POST['l']
        reg = request.POST['r']
        type = request.POST['ty']
        vac=request.POST['v']
        sal=request.POST['s']
        exp=request.POST['exp']
        date=request.POST['dead']
        appli=request.POST['appli']
        desc = request.POST['jd']
        c_det=request.POST['c']
        tag = request.POST['tg']
        c_desc = request.POST['cd']
        web = request.POST['w']
        fbook = request.POST['fb']
        twit=request.POST['tw']
        linkd=request.POST['ld']
        logo= request.FILES['logo']
        j=Jobpost.objects.create(image=img,email=email,title=tit,location=loc,region=reg,type=type,description=desc,company=c_det,tagline=tag,companydesc=c_desc,
                                 website=web,facebook=fbook,twitter=twit,linkedin=linkd,logo=logo,vaccancy=vac,salary=sal,experience=exp,application_deadline=date,published=appli)
        j.save()
        return redirect('employee:home')
    return render(request,'jobpost.html')


class Jobdetails(DetailView):
    model=Jobpost
    template_name='jobdetails.html'
    context_object_name = 'job'
