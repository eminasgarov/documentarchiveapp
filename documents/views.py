from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from documents.models import Procedure
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q 
# Create your views here.

@login_required(login_url = 'login')
def procedures(request):
    procedures              = Procedure.objects.order_by('-created_date')
    paginator               = Paginator(procedures, 10)
    page                    = request.GET.get('page')
    paged_procedures        = paginator.get_page(page)
    procedures_count        = procedures.count()
    
    data = {
        'procedures':           paged_procedures,
        'procedures_count':     procedures_count,
    }
    return render(request, 'pages/procedures.html', data)

@login_required(login_url = 'login')
def procedure_search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            procedures = Procedure.objects.order_by('-created_date').filter(Q(procedure_name__icontains=keyword))
            procedures_count   = procedures.count()
    data = {
        'procedures': procedures,
        'procedures_count': procedures_count,
    }
    return render(request, 'pages/procedures.html', data)


