from django.forms import forms
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.template import loader, RequestContext
import django_excel as excel
from tablib import Dataset


# Create your views here.
from onlypage.admin import Camerapost
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


def simple_upload(request):
        if request.method == 'POST':
            person_resource = Camerapost()
            dataset = Dataset()
            new_persons = request.FILES['myfile']

            imported_data = dataset.load(new_persons.read())
            result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

            if not result.has_errors():
                person_resource.import_data(imported_data, dry_run=False)  # Actually import now

        return render(request, 'upload_form.html')گ

