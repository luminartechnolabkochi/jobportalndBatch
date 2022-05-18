from django.urls import path
from employer import views
urlpatterns=[
    path("emphome",views.EmployerHomeView.as_view(),name="e-home"),
    path("profiles/add",views.EmployerProfileCreateView.as_view(),name="emp-profile"),
    path("profiles/details",views.EMployeeProfileDetailView.as_view(),name="emp-detail"),
    path("jobs/add",views.JobCreateView.as_view(),name="emp-addjob"),
    path("jobs/all",views.EmployerJobListView.as_view(),name="emp-listjob")
]