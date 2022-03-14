from .models import DocumentVariation, Department, DocumentSection


def doc_sec_filter_link(request):
    document_sections = DocumentSection.objects.all()
    return dict(document_sections=document_sections)

def doc_filter_link(request):
    docs = DocumentVariation.objects.all()
    return dict(docs=docs)


def dep_filter_link(request):
    departments = Department.objects.all()
    return dict(departments=departments) 
