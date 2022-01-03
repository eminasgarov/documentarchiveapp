from .models import Document, Department

def doc_filter_link(request):
    documents = Document.objects.all()
    return dict(documents=documents)


def dep_filter_link(request):
    departments = Department.objects.all()
    return dict(departments=departments) 
   