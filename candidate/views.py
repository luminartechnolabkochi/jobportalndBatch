from django.urls import reverse_lazy
from django.shortcuts import render
from candidate.forms import CandidateProfileForm
from django.views.generic import TemplateView,CreateView
from candidate.models import CandidateProfile
from employer.models import Jobs
# Create your views here.


class CandidateHomeView(TemplateView):
    template_name = "cand-home.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        qs=Jobs.objects.all()
        context["jobs"]=qs
        return context


class CandidateProfileCreateView(CreateView):
    model=CandidateProfile
    form_class = CandidateProfileForm
    template_name = "cand-profile.html"
    success_url = reverse_lazy("cand-home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

