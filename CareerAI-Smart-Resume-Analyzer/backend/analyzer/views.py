from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.exceptions import ValidationError
from .models import Resume,MatchResult
from .serializers import ResumeSerializer,MatchSerializer
from .parser import extract_text
from .matcher import analyze
from jobs.models import Job
class ResumeListCreateView(generics.ListCreateAPIView):
 serializer_class=ResumeSerializer;parser_classes=[MultiPartParser,FormParser]
 def get_queryset(self): return Resume.objects.filter(user=self.request.user)
 def perform_create(self,serializer):
  f=self.request.FILES.get("file")
  if not f: raise ValidationError({"file":"Please select a PDF or DOCX file."})
  if f.size>5*1024*1024: raise ValidationError({"file":"Maximum file size is 5 MB."})
  try: text=extract_text(f)
  except Exception as e: raise ValidationError({"file":str(e)})
  serializer.save(user=self.request.user,extracted_text=text,title=self.request.data.get("title") or f.name)
class ResumeDetailView(generics.RetrieveDestroyAPIView):
 serializer_class=ResumeSerializer
 def get_queryset(self): return Resume.objects.filter(user=self.request.user)
class AnalyzeMatchView(APIView):
 def post(self,request):
  try: resume=Resume.objects.get(id=request.data.get("resume_id"),user=request.user)
  except Resume.DoesNotExist: return Response({"detail":"Resume not found."},status=404)
  try: job=Job.objects.get(id=request.data.get("job_id"))
  except Job.DoesNotExist: return Response({"detail":"Job not found."},status=404)
  result=analyze(resume.extracted_text,job.description+" "+job.requirements)
  obj=MatchResult.objects.create(user=request.user,resume=resume,job=job,**{k:result[k] for k in ("score","matched_skills","missing_skills","recommendations")})
  return Response(MatchSerializer(obj).data,status=status.HTTP_201_CREATED)
class MatchHistoryView(generics.ListAPIView):
 serializer_class=MatchSerializer
 def get_queryset(self): return MatchResult.objects.filter(user=self.request.user).select_related("resume","job")
class DashboardView(APIView):
 def get(self,request):
  resumes=Resume.objects.filter(user=request.user).count()
  matches=MatchResult.objects.filter(user=request.user)
  avg=round(sum(x.score for x in matches)/matches.count()) if matches.exists() else 0
  return Response({"resume_count":resumes,"match_count":matches.count(),"average_match_score":avg,"recent_matches":MatchSerializer(matches[:5],many=True).data})
