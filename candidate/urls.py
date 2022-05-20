from django.urls import path
from candidate import views

urlpatterns=[
    path("home",views.CandidateHomeView.as_view(),name="cand-home"),
    path("profiles/add",views.CandidateProfileCreateView.as_view(),name="cand-addprofile")
]