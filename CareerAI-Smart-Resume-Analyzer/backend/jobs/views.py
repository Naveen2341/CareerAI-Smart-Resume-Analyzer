from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Job,SavedJob
from .serializers import JobSerializer
class JobViewSet(viewsets.ModelViewSet):
 serializer_class=JobSerializer
 def get_queryset(self):
  qs=Job.objects.all()
  q=self.request.query_params.get("search","")
  if q: qs=qs.filter(Q(title__icontains=q)|Q(company__icontains=q)|Q(description__icontains=q)|Q(requirements__icontains=q))
  return qs
 def perform_create(self,serializer): serializer.save(posted_by=self.request.user)
 def perform_update(self,serializer):
  if self.get_object().posted_by_id!=self.request.user.id: from rest_framework.exceptions import PermissionDenied; raise PermissionDenied("Only the job author can edit.")
  serializer.save()
 def perform_destroy(self,instance):
  if instance.posted_by_id!=self.request.user.id: from rest_framework.exceptions import PermissionDenied; raise PermissionDenied("Only the job author can delete.")
  instance.delete()
 @action(detail=True,methods=["post"])
 def save(self,request,pk=None):
  job=self.get_object();saved,created=SavedJob.objects.get_or_create(user=request.user,job=job)
  if not created: saved.delete();return Response({"saved":False})
  return Response({"saved":True},status=status.HTTP_201_CREATED)
