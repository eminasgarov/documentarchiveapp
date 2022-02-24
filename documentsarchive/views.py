from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from documents.models import Document
from django.shortcuts import render, get_object_or_404
from category.models import DocumentVariation


@login_required(login_url = 'login')
def home(request):
        
    if request.user.userprofile.is_management:
        documents                  = Document.objects.all().order_by('-created_date')
        last_documents             = Document.objects.all().order_by('-created_date')[:7]
        featured_documents         = Document.objects.all().order_by('-created_date').filter(is_featured=True)
    else:
        documents                  = Document.objects.filter(department=request.user.userprofile.department).order_by('-created_date')
        last_documents             = Document.objects.filter(department=request.user.userprofile.department).order_by('-created_date')[:7]
        featured_documents         = Document.objects.filter(department=request.user.userprofile.department).order_by('-created_date').filter(is_featured=True)


    data = {
        'documents':                    documents,          
        'last_documents':               last_documents,
        'featured_documents':           featured_documents,
    }
    return render(request, 'home.html', data)