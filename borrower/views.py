
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from borrower.models import Borrower
from borrower.forms import BorrowerForm
# Create your views here.


# Borrower Views
class BorrowerListView(ListView):
    model = Borrower
    template_name = 'borrower/borrower_list.html'
    context_object_name = 'borrowers'
    paginate_by = 10

class BorrowerDetailView(DetailView):
    model = Borrower
    template_name = 'borrower/borrower_detail.html'
    context_object_name = 'borrower'

class BorrowerCreateView(CreateView):
    model = Borrower
    form_class = BorrowerForm
    template_name = 'borrower/borrower_form.html'
    success_url = reverse_lazy('borrower_list')

class BorrowerUpdateView(UpdateView):
    model = Borrower
    form_class = BorrowerForm
    template_name = 'borrower/borrower_form.html'
    success_url = reverse_lazy('borrower_list')

class BorrowerDeleteView(DeleteView):
    model = Borrower
    template_name = 'borrower/borrower_confirm_delete.html' # Create this template
    success_url = reverse_lazy('borrower_list')
