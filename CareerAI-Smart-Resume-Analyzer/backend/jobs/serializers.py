from rest_framework import serializers
from .models import Job
class JobSerializer(serializers.ModelSerializer):
 is_saved=serializers.SerializerMethodField()
 class Meta: model=Job;fields=("id","title","company","location","employment_type","description","requirements","source_url","created_at","is_saved");read_only_fields=("id","created_at","is_saved")
 def get_is_saved(self,obj):
  u=self.context["request"].user
  return obj.saved_by.filter(user=u).exists()
