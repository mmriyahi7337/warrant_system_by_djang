from django.forms import forms
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.template import loader, RequestContext
import django_excel as excel

# Create your views here.


from .models import Camera


def index(request):
    if request.POST:
        n = request.POST.get('serial')
        m = Camera.objects.filter(Barcode=n)
        template = loader.get_template('index.html')

        if m.first() is None:
            m = -1
            return HttpResponse(template.render(request=request, context={'cam': m}))
        template = loader.get_template('index.html')

        return HttpResponse(template.render(request=request, context={'cam': m.first()}))

    template = loader.get_template('index.html')

    return HttpResponse(template.render(request=request))


class UploadFileForm(forms.Form):
    file = forms.FileField()


def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv",
                                       file_name="download")
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Excel file upload and download example',
            'header': ('فایل اکسل خود را وارد کنید:')
        })


def import_sheet(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                name_columns_by_row=100,
                model=Camera,
                mapdict=['id', 'name', 'Startdayofwarranty','Enddateofwarranty','Barcode'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {'form': form})
