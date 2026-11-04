from django.conf import settings
from django.db import models
class Resume(models.Model):
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="resumes")
 title=models.CharField(max_length=160,default="My Resume")
 file=models.FileField(upload_to="resumes/")
 extracted_text=models.TextField(blank=True)
 uploaded_at=models.DateTimeField(auto_now_add=True)
 class Meta: ordering=["-uploaded_at"]
 def __str__(self): return self.title
class MatchResult(models.Model):
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="match_results")
 resume=models.ForeignKey(Resume,on_delete=models.CASCADE,related_name="matches")
 job=models.ForeignKey("jobs.Job",on_delete=models.CASCADE,related_name="matches")
 score=models.PositiveSmallIntegerField()
 matched_skills=models.JSONField(default=list)
 missing_skills=models.JSONField(default=list)
 recommendations=models.JSONField(default=list)
 created_at=models.DateTimeField(auto_now_add=True)
 class Meta: ordering=["-created_at"]
