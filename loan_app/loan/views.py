from django.shortcuts import render
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .models import TransactionId
# Create your views here.

@staff_member_required(login_url='login')
def search(request):
    query = request.GET.get("query")
    search_result = []
    if query:
        search_result = TransactionId.objects.filter(transaction_id=query)
        
        if not search_result:
            messages.info(request, f'No matching history for {query}.') # return transaction_id if not found with a simple message
    else:
        messages.warning(request, "Please enter a transaction_id to search")
    return render(request, 'loan/search.html', {'search_result':search_result, 'query':query})
