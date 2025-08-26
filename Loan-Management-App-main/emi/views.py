
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from emi.models import EMI
from emi.forms import EMIForm
# Create your views here.



# EMI Views
class EMIListView(ListView):
    model = EMI
    template_name = 'emi/emi_list.html'
    context_object_name = 'emis'
    paginate_by = 10

class EMIDetailView(DetailView):
    model = EMI
    template_name = 'emi/emi_detail.html'
    context_object_name = 'emi'

class EMICreateView(CreateView):
    model = EMI
    form_class = EMIForm
    template_name = 'emi/emi_form.html'
    success_url = reverse_lazy('emi_list')

class EMIUpdateView(UpdateView):
    model = EMI
    form_class = EMIForm
    template_name = 'emi/emi_form.html'
    success_url = reverse_lazy('emi_list')

class EMIDeleteView(DeleteView):
    model = EMI
    template_name = 'emi/emi_confirm_delete.html'
    success_url = reverse_lazy('emi_list')
