from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from category.models import DocumentVariation
from documents.models import Document
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render
from django.db.models import Count
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from datetime import datetime
from django.contrib.auth.models import User
from accounts.models import UserProfile

    

@receiver(user_logged_in)
def got_online(sender, user, request, **kwargs):    
    user.userprofile.is_online = True
    user.userprofile.save()
    
    
@receiver(user_logged_out)
def user_logged_out(sender, user, request, **kwargs):
     user.userprofile.last_logout = datetime.now()
     user.userprofile.is_online = False
     user.userprofile.save()


@login_required(login_url = 'login')
def home(request):
    
    users         = User.objects.all().count()
    users_online  = UserProfile.objects.filter(is_online=True).count()
    users_offline = UserProfile.objects.filter(is_online=False).count()
    
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
        'users':                        users,
        'users_online':                 users_online,
        'users_offline':                users_offline,
    }
    return render(request, 'home.html', data)



     

