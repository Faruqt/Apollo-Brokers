from django.http import JsonResponse
from django.shortcuts import render
from .forms import UploadXMLform


def upload_page(request):
    
    form = UploadXMLform()
    if request.method == 'POST':
        form = UploadXMLform(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
        else:
            form = UploadXMLform()
        # TODO: Convert the submitted XML file into a JSON object and return to the user.
        return JsonResponse({})

    context = {'form' : form}
    return render(request, "upload_page.html", context)
