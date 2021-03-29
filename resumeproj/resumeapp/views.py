from django.shortcuts import render
from .forms import *
from .models import *
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self,request):
        form=ResumeForm()
        candidates=Resume.objects.all()
        return render(request,'resumeapp/home.html',{'form':form,'candidates':candidates})
    def post(self,request):
        form=ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return render(request,'resumeapp/home.html',{'form':form})
class CandidateView(View):
    def get(self,request,pk):
        candidate=Resume.objects.get(pk=pk)
        return render(request,'resumeapp/candidate.html',{'candidate':candidate})
    
