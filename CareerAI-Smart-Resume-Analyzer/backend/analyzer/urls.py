from django.urls import path
from .views import ResumeListCreateView,ResumeDetailView,AnalyzeMatchView,MatchHistoryView,DashboardView
urlpatterns=[path("resumes/",ResumeListCreateView.as_view()),path("resumes/<int:pk>/",ResumeDetailView.as_view()),path("matches/analyze/",AnalyzeMatchView.as_view()),path("matches/",MatchHistoryView.as_view()),path("dashboard/",DashboardView.as_view())]
