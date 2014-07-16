from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext
from django import forms

#pdfs
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter 
from StringIO import StringIO

def home(request):
	return render_to_response('home.html')

class FileForm(forms.Form):
	upload_file = forms.FileField()

def parse_PDF(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            efl = request.FILES['upload_file'].read()
            memory_file = StringIO(efl)
            parser = PDFParser(memory_file)
            document = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            retstr = StringIO()
            laparams = LAParams()
            codec = 'utf-8'
            device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
            interpreter = PDFPageInterpreter(rsrcmgr, device)

            for page in PDFPage.create_pages(document):
                interpreter.process_page(page)
                data = retstr.getvalue()
            #u = data.decode('cp1251')
            #s = u.encode('utf-8')
            return render_to_response('pdfs/parsePDF.html', 
                {'parse': data})
        else:
        	return render_to_response('genericformprompt.html',
            	{'form': form, 'description': 'Select a PDF...', 'enctype':'multipart/form-data'})
    else:
        form = FileForm()
        return render_to_response('genericformprompt.html',
            {'form': form, 'description': 'Select a PDF...', 'enctype':'multipart/form-data'},
            context_instance=RequestContext(request))