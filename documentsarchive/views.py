from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from documents.models import Procedure


@login_required(login_url = 'login')
def home(request):
    procedures              = Procedure.objects.order_by('-created_date')
    procedures_count        = procedures.count()
    last_procedures         = Procedure.objects.order_by('-created_date')[:7]
    
    data = {
        "procedures": procedures,
        "procedures_count": procedures_count,
        "last_procedures": last_procedures,
    }
    return render(request, 'home.html', data)