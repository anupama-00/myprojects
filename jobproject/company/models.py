from django.db import models

# Create your models here.
class Jobpost(models.Model):
    image=models.ImageField(upload_to="images")
    email=models.EmailField()
    title=models.CharField(max_length=30)
    location=models.CharField(max_length=20)
    region=models.CharField(max_length=20)
    type=models.CharField(max_length=20)
    vaccancy=models.IntegerField(default=0)
    published=models.DateField(auto_now=True)
    experience=models.CharField(max_length=20,default="")
    salary=models.IntegerField(default=0)
    application_deadline=models.DateField(auto_now=True)
    description=models.TextField()
    company=models.CharField(max_length=50)
    tagline=models.CharField(max_length=30)
    companydesc=models.TextField()
    website=models.CharField(max_length=30)
    facebook=models.CharField(max_length=30)
    twitter=models.CharField(max_length=30)
    linkedin=models.CharField(max_length=30)
    logo=models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


