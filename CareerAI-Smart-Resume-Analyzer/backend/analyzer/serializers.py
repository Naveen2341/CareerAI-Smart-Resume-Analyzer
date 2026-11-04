from rest_framework import serializers
from .models import Resume,MatchResult
class ResumeSerializer(serializers.ModelSerializer):
 class Meta: model=Resume;fields=("id","title","file","uploaded_at");read_only_fields=("id","uploaded_at")
class MatchSerializer(serializers.ModelSerializer):
 resume_title=serializers.CharField(source="resume.title",read_only=True)
 job_title=serializers.CharField(source="job.title",read_only=True)
 company=serializers.CharField(source="job.company",read_only=True)
 class Meta: model=MatchResult;fields=("id","resume","resume_title","job","job_title","company","score","matched_skills","missing_skills","recommendations","created_at")
