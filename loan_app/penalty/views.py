
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from penalty.models import Penalty
from penalty.forms import PenaltyForm

# Create your views here.

# Penalty Views
class PenaltyListView(ListView):
    model = Penalty
    template_name = 'penalty/penalty_list.html'
    context_object_name = 'penalties'
    paginate_by = 10

class PenaltyDetailView(DetailView):
    model = Penalty
    template_name = 'penalty/penalty_detail.html'
    context_object_name = 'penalty'

class PenaltyCreateView(CreateView):
    model = Penalty
    form_class = PenaltyForm
    template_name = 'penalty/penalty_form.html'
    success_url = reverse_lazy('penalty_list')

class PenaltyUpdateView(UpdateView):
    model = Penalty
    form_class = PenaltyForm
    template_name = 'penalty/penalty_form.html'
    success_url = reverse_lazy('penalty_list')

class PenaltyDeleteView(DeleteView):
    model = Penalty
    template_name = 'penalty/penalty_confirm_delete.html'
    success_url = reverse_lazy('penalty_list')