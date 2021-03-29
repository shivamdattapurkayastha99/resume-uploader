from django.db import models

# Create your models here.
STATE_CHOICES=(
    ('WESTBENGAL','WESTBENGAL'),
    ('MAHARASHTRA','MAHARASHTRA'),
)
class Resume(models.Model):
    name=models.CharField(max_length=20)
    dob=models.DateTimeField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=10)
    locality=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=50)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job_city=models.CharField(max_length=20)
    profile_image=models.ImageField(upload_to='profileimg',blank=True)
    my_file=models.FileField(upload_to='doc',blank=True)


