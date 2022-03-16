from django.http import JsonResponse
from django.shortcuts import render

# import XML upload form
from .forms import Upload_XML_form

# import XML_to_json function from utils.py file
from .utils import XML_to_json

def upload_page(request):

    # TODO: Convert the submitted XML file into a JSON object and return to the user.

    form = Upload_XML_form()
    if request.method == 'POST':
        form = Upload_XML_form(request.POST, request.FILES)
        if form.is_valid():
            converted_XML = XML_to_json(request.FILES['file'])
        else:
            form = UploadXMLform()
        return JsonResponse(converted_XML)

    context = {
        'form' : form,
        }
    return render(request, "upload_page.html", context)
