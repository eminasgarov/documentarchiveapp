from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from documents.models import Document


@login_required(login_url = 'login')
def home(request):
    documents                  = Document.objects.order_by('-created_date')
    last_documents             = Document.objects.order_by('-created_date')[:7]
    featured_documents          = Document.objects.order_by('-created_date').filter(is_featured=True)

    
    data = {
        'documents':                    documents,          
        'last_documents':               last_documents,
        'featured_documents':             featured_documents,
    }
    return render(request, 'home.html', data)