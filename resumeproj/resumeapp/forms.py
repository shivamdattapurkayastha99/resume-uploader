from django import forms
from .models import *
GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female'),
]
JOB_CITY_CHOICE=[
    ('Mumbai','Mumbai'),
    ('Kolkata','Kolkata'),
]
class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(label='Preffered Job Location',choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields=['id','name','dob','gender','locality','city','pin','state','mobile','job_city','profile_image','my_file']
        labels={'name':'Full Name','dob':'Date of Birth','pin':'Pin Code','mobile':'Mobile No','email':'Email Id','profile_image':'Profile Image','my_file':'Document'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-comtrol'}),
            'dob':forms.DateInput(attrs={'class':'form-comtrol','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-comtrol'}),
            'city':forms.TextInput(attrs={'class':'form-comtrol'}),
            'pin':forms.NumberInput(attrs={'class':'form-comtrol'}),
            'state':forms.Select(attrs={'class':'form-comtrol'}),
            'mobile':forms.NumberInput(attrs={'class':'form-comtrol'}),
            'email':forms.EmailInput(attrs={'class':'form-comtrol'}),
            
        }