from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from category.models import Department, DocumentVariation
from documents.models import Document
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.

@login_required(login_url = 'login')
def documents(request, document_type_slug=None):
    document_types          = None
    documents               = None

    if document_type_slug != None:
        if request.user.userprofile.is_management:
            document_types          = get_object_or_404(DocumentVariation, slug=document_type_slug)
            documents               = Document.objects.filter(document_type=document_types).order_by('-created_date')
            documents_count         = documents.count()
        else:
            document_types          = get_object_or_404(DocumentVariation, slug=document_type_slug)
            documents               = Document.objects.filter(Q(document_type=document_types, department=request.user.userprofile.department) | Q(document_type=document_types, access_for_all=True)).order_by('-created_date')
            documents_count         = documents.count()
    
    else:
        if request.user.userprofile.is_management:
            documents               = Document.objects.all().order_by('-created_date')
            documents_count         = documents.count()
        else:
            documents               = Document.objects.filter(Q(department=request.user.userprofile.department) | Q(access_for_all=True)).order_by('-created_date')
            documents_count         = documents.count()
    
    paginator               = Paginator(documents, 15)
    page                    = request.GET.get('page')
    paged_documents         = paginator.get_page(page)
    documents_count         = documents.count()
        
    data = {
        'documents':             paged_documents,
        'documents_count':       documents_count,
    }
    return render(request, 'pages/documents.html', data)


@login_required(login_url = 'login')
def search(request):
    
    if request.user.userprofile.is_management:
        documents               = Document.objects.all().order_by('-created_date')
    else:
        documents               = Document.objects.order_by('-created_date').filter(Q(department=request.user.userprofile.department) | Q(access_for_all=True))
    
    department_search       = Department.objects.values_list('department', flat=True).distinct()
    document_type_search    = DocumentVariation.objects.values_list('document_type', flat=True).distinct()
    
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            documents           = documents.filter(document_name__icontains=keyword)
            documents_count     = documents.count()
    
    if 'department' in request.GET:
        department = request.GET['department']
        if department:
            documents           = documents.filter(department__department__iexact=department)
            documents_count     = documents.count()
            
    if 'document_type' in request.GET:
        document_type = request.GET['document_type']
        if document_type:
            documents           = documents.filter(document_type__document_type__iexact=document_type)
            documents_count     = documents.count()
            
    paginator           = Paginator(documents, 15)
    page                = request.GET.get('page')
    paged_documents     = paginator.get_page(page)
    documents_count     = documents.count()
            
    data = {
        'document_type_search':    document_type_search,
        'department_search':       department_search,
        'documents':               paged_documents,
        'documents_count':         documents_count,

    }
    return render(request, 'pages/search.html', data)
