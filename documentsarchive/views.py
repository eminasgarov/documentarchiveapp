from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from category.models import DocumentVariation
from documents.models import Document
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render
from django.db.models import Count



@login_required(login_url = 'login')
def home(request):
    
    type_id         = []
    type_count      = []
    document_types  = []
    stat_objects    = zip(document_types, type_count)
            
    if request.user.userprofile.is_management:
        documents                  = Document.objects.all().order_by('-created_date')
        last_documents             = Document.objects.all().order_by('-created_date')[:10]
        featured_documents         = Document.objects.all().order_by('-created_date').filter(is_featured=True)
        documents_dictionary       = Document.objects.values_list('document_type').annotate(Count('document_type')).order_by()
        
        for key, value in documents_dictionary:
            type_id.append(key)
            type_count.append(value)
        
        document_types_list        = DocumentVariation.objects.values_list('document_type', flat=True).filter(pk__in=type_id)
        
        for i in document_types_list:
            document_types.append(i)
            
    else:
        documents                  = Document.objects.filter(Q(department=request.user.userprofile.department) | Q(access_for_all=True)).order_by('-created_date')
        last_documents             = Document.objects.filter(Q(department=request.user.userprofile.department) | Q(access_for_all=True)).order_by('-created_date')[:10]
        featured_documents         = Document.objects.filter(Q(department=request.user.userprofile.department) | Q(access_for_all=True)).order_by('-created_date').filter(is_featured=True)
        documents_dictionary       = Document.objects.filter(Q(department=request.user.userprofile.department) | Q(access_for_all=True)).values_list('document_type').annotate(Count('document_type')).order_by()
        
        for key, value in documents_dictionary:
            type_id.append(key)
            type_count.append(value)
        
        document_types_list        = DocumentVariation.objects.values_list('document_type', flat=True).filter(pk__in=type_id)
        for i in document_types_list:
            document_types.append(i)
    
    sum_types       = sum(type_count)
    

    data = {
        'documents':                    documents,          
        'last_documents':               last_documents,
        'featured_documents':           featured_documents,
        'document_types':               document_types,
        'type_count':                   type_count,
        'sum_types':                    sum_types,
        'stat_objects':                 stat_objects,
    }
    return render(request, 'home.html', data)