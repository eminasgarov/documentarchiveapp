from .models import Document, Department, DocumentSection

def doc_sec_filter_link(request):
    document_sections = DocumentSection.objects.all()
    return dict(document_sections=document_sections)

def doc_filter_link(request):
    documents = Document.objects.all()
    return dict(documents=documents)


def dep_filter_link(request):
    departments = Department.objects.all()
    return dict(departments=departments) 
   