from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView
from employer.forms import EmployerProfileForm,JobForm
from employer.models import EmployerProfile,Jobs
class EmployerHomeView(TemplateView):
    template_name = "emp-home.html"


class EmployerProfileCreateView(CreateView):
    model=EmployerProfile
    form_class = EmployerProfileForm
    template_name = "emp-profile.html"
    success_url = reverse_lazy("e-home")


    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     form=EmployerProfileForm(request.POST,files=request.FILES)
    #     if form.is_valid():
    #        profile= form.save(commit=False)
    #        profile.user=request.user
    #        profile.save()
    #        print("profile created")
    #        return redirect("e-home")
    #     else:
    #         return render(request,self.template_name,{"form":form})

class EMployeeProfileDetailView(TemplateView):
    template_name = "emp-myprofile.html"


class JobCreateView(CreateView):
    model=Jobs
    form_class =JobForm
    template_name = "emp-postjob.html"
    success_url =reverse_lazy("e-home")

    def form_valid(self, form):
        form.instance.posted_by=self.request.user
        return super().form_valid(form)

class EmployerJobListView(ListView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "emp-joblist.html"

    def get_queryset(self):
        return Jobs.objects.filter(posted_by=self.request.user)
