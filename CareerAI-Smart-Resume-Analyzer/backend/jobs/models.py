from django.conf import settings
from django.db import models
class Job(models.Model):
 title=models.CharField(max_length=180)
 company=models.CharField(max_length=160)
 location=models.CharField(max_length=160,blank=True)
 employment_type=models.CharField(max_length=80,blank=True)
 description=models.TextField()
 requirements=models.TextField(blank=True)
 source_url=models.URLField(blank=True)
 posted_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="posted_jobs")
 created_at=models.DateTimeField(auto_now_add=True)
 class Meta: ordering=["-created_at"]
 def __str__(self): return f"{self.title} - {self.company}"
class SavedJob(models.Model):
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
 job=models.ForeignKey(Job,on_delete=models.CASCADE,related_name="saved_by")
 created_at=models.DateTimeField(auto_now_add=True)
 class Meta: unique_together=("user","job")
