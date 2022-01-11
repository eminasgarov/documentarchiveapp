from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from documents.models import KISDocument


@login_required(login_url = 'login')
def home(request):
    kis_documents                  = KISDocument.objects.order_by('-created_date')
    last_kis_documents             = KISDocument.objects.order_by('-created_date')[:7]
    featured_kis_documents          = KISDocument.objects.order_by('-created_date').filter(is_featured=True)

    
    data = {
        'kis_documents':                    kis_documents,          
        'last_kis_documents':               last_kis_documents,
        'featured_kis_documents':             featured_kis_documents,
    }
    return render(request, 'home.html', data)