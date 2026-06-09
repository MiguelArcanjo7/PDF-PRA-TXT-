import fitz
from django.shortcuts import render
from django.http import HttpResponse

def upload_pdf(request):
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        pdf_file = request.FILES['pdf_file']
        doc = fitz.open(stream = pdf_file.read(), filetype="PDF") # Ler PDF
        texto_completo = ""
        for pagina in doc:
            texto_completo += pagina.get_text()
        doc.close()
        response = HttpResponse(texto_completo, content_type='text/plain')
        response['Content-Diposition'] = 'attachment; filename="resultado.txt"'
        return response
    return render(request, 'meuapp/upload.html')

# Create your views here.
