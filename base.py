import xml_data_handler
import re

def print_nicely(thingToPrint):
    for i in thingToPrint:
        print(i)



#location = "/home/jo/Desktop/basic_maths.jpg"
location = "/home/jo/Desktop/pasta_cooked.jpg"
#location = "/home/jo/Desktop/image.jpg"
#location = "/home/jo/Desktop/villa1.JPG"

#metadata_regex_ord = r"(?<=\\[0-9A-Za-z]{3})([A-Za-z .:\-\/]{3,150}|[0-9]{1,4}:[0-9]{1,4}:[0-9]{1,4})"
metadata_regex_ord = r"(?<=\\x[0-9A-Za-z]{2})([A-Za-z0-9 ]{1}[A-Za-z0-9 .:#-/]{3,150})(?=\\x)"
metadata_regex_xml = r"(<\?xpa.*meta>)"

file = open(location, "rb")
imgdata = file.read()
file.close()

imgdata = str(imgdata)

metadata_ord = []
metadata_xml = []

#print(imgdata[30000:60000])

#FINDING ORDINARY METADATA IN IMAGE
if re.findall(metadata_regex_ord, imgdata):
    for i in re.findall(metadata_regex_ord, imgdata):
        match = re.search(r"([A-Za-z0-9 .:/-]{8,150})", i)
        if match:
            metadata_ord.append(match.group(0))


#FINDING DATA FROM XML CONTAINED WITHIN THE IMAGE
if re.findall(metadata_regex_xml, imgdata):
    for i in re.findall(metadata_regex_xml, imgdata):
        metadata_xml.append(i)

xml_meta_touples = xml_data_handler.handle_xml_meta(metadata_xml)

print_nicely(metadata_ord)

for key, value in xml_meta_touples.items():
    if value is not "0" and key is not "WebStatement":
       print(key, " ", value)






