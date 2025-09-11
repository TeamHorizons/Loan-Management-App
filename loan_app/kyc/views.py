
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from kyc.models import KYC
from kyc.forms import KYCForm
# Create your views here.




# KYC Views
class KYCListView(ListView):
    model = KYC
    template_name = 'kyc/kyc_list.html'
    context_object_name = 'kycs'
    paginate_by = 10

class KYCDetailView(DetailView):
    model = KYC
    template_name = 'kyc/kyc_detail.html'
    context_object_name = 'kyc'

class KYCCreateView(CreateView):
    model = KYC
    form_class = KYCForm
    template_name = 'kyc/kyc_form.html'
    success_url = reverse_lazy('kyc_list')

class KYCUpdateView(UpdateView):
    model = KYC
    form_class = KYCForm
    template_name = 'kyc/kyc_form.html'
    success_url = reverse_lazy('kyc_list')

class KYCDeleteView(DeleteView):
    model = KYC
    template_name = 'kyc/kyc_confirm_delete.html'
    success_url = reverse_lazy('kyc_list')
