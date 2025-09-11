
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from document.forms import DocumentForm
from document.models import Document



# Create your views here.


# Document Views
class DocumentListView(ListView):
    model = Document
    template_name = 'document/document_list.html'
    context_object_name = 'documents'
    paginate_by = 10

class DocumentDetailView(DetailView):
    model = Document
    template_name = 'document/document_detail.html'
    context_object_name = 'document'

class DocumentCreateView(CreateView):
    model = Document
    form_class = DocumentForm
    template_name = 'document/document_form.html'
    success_url = reverse_lazy('document_list')

class DocumentUpdateView(UpdateView):
    model = Document
    form_class = DocumentForm
    template_name = 'document/document_form.html'
    success_url = reverse_lazy('document_list')

class DocumentDeleteView(DeleteView):
    model = Document
    template_name = 'document/document_confirm_delete.html'
    success_url = reverse_lazy('document_list')