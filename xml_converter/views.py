from django.http import JsonResponse
from django.shortcuts import render

# import XML upload form
from .forms import Upload_XML_form

# import json and xmltodict packages
import json
import xmltodict


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


def XML_to_json(file):
    # open xml file
    with file as xml_file:
        data = xmltodict.parse(xml_file.read())

    # close xml file after parsing the content
    xml_file.close()

    # convert content of xml file to json
    json_data = json.dumps(data)


    # parse json_data from json string to python dictionary:
    converted = json.loads(json_data)

    # change 'None' keyword to empty string "" 
    for key in converted:
        if converted[key] == None:
            converted[key] = ""

    return converted


