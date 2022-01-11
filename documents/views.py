from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from category.models import Department, Document
from documents.models import KISDocument
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

@login_required(login_url = 'login')
def kis_documents(request, document_type_slug=None):
    document_types              = None
    kis_documents               = None
    
    if document_type_slug != None:
        document_types          = get_object_or_404(Document, slug=document_type_slug)
        kis_documents           = KISDocument.objects.filter(document_type=document_types).order_by('-created_date')
        paginator               = Paginator(kis_documents, 10)
        page                    = request.GET.get('page')
        paged_kis_documents     = paginator.get_page(page)
        kis_documents_count     = kis_documents.count()
    
    else:
        kis_documents           = KISDocument.objects.all().order_by('-created_date')
        paginator               = Paginator(kis_documents, 10)
        page                    = request.GET.get('page')
        paged_kis_documents     = paginator.get_page(page)
        kis_documents_count     = kis_documents.count()
        
    data = {
        'kis_documents':           paged_kis_documents,
        'kis_documents_count':     kis_documents_count,
    }
    return render(request, 'pages/kis_documents.html', data)


@login_required(login_url = 'login')
def search(request):
    kis_documents           = KISDocument.objects.order_by('-created_date')
    department_search       = Department.objects.values_list('department', flat=True).distinct()
    document_type_search    = Document.objects.values_list('document_type', flat=True).distinct()
    
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            kis_documents           = kis_documents.filter(kis_document_name__icontains=keyword)
            kis_documents_count     = kis_documents.count()
    
    if 'department' in request.GET:
        department = request.GET['department']
        if department:
            kis_documents           = kis_documents.filter(department__department__iexact=department)
            kis_documents_count     = kis_documents.count()
            
    if 'document_type' in request.GET:
        document_type = request.GET['document_type']
        if document_type:
            kis_documents           = kis_documents.filter(document_type__document_type__iexact=document_type)
            kis_documents_count     = kis_documents.count()
            
    paginator               = Paginator(kis_documents, 10)
    page                    = request.GET.get('page')
    paged_kis_documents     = paginator.get_page(page)
    kis_documents_count     = kis_documents.count()
            
    data = {
        'document_type_search':    document_type_search,
        'department_search':       department_search,
        'kis_documents':           paged_kis_documents,
        'kis_documents_count':     kis_documents_count,

    }
    return render(request, 'pages/search.html', data)
