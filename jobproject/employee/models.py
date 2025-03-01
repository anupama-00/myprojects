
from django.db import models

from company.models import Jobpost

from user.models import CustomUser


class Jobapply(models.Model):
    job=models.ForeignKey(Jobpost,on_delete=models.CASCADE,related_name='jobs')
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='users')
    resume=models.FileField(upload_to='files')
    current_CTC = models.IntegerField(default=0)
    expected_CTC=models.IntegerField(default=0)
    interview_date=models.TextField()
    apply_status=models.CharField(max_length=20,default="pending")

    def __str__(self):
        return self.job.title



class SavedJob(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobpost, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job.title

