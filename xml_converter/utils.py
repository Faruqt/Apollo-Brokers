# import json and xmltodict packages
import json
import xmltodict

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


