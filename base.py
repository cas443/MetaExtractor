import xml_meta_handler
import re



#location = "/home/jo/Desktop/basic_maths.jpg"
location = "/home/jo/Desktop/pasta_cooked.jpg"
#location = "/home/jo/Desktop/image.jpg"
#location = "/home/jo/Desktop/villa1.JPG"

metadata_regex_ord = r"(?<=\\x[0-9A-Za-z]{2})([A-Za-z0-9 ]{1}[A-Za-z0-9 .:#-/]{3,150})(?=\\x)"
metadata_regex_xml = r"(<\?xpa.*meta>)"

file = open(location, "rb")
imgdata = file.read()
file.close()

imgdata = str(imgdata)

metadata_ord = []
metadata_xml = []
dupes = []

#print(imgdata[:50000])

print("[+] METADATA FROM FILE: ", re.search(r"(?:.*/)(.*)(?=)", location).group(1))


#FINDING ORDINARY METADATA IN IMAGE
if re.findall(metadata_regex_ord, imgdata):
    for i in re.findall(metadata_regex_ord, imgdata):
        match = re.search(r"([A-Za-z0-9 .:/-]{4,150})", i)
        if match and match not in dupes:
            metadata_ord.append(match.group(0))
            dupes.append(match)
metadata_ord.sort(key=len, reverse=True)


#FINDING DATA FROM XML CONTAINED WITHIN THE IMAGE
if re.findall(metadata_regex_xml, imgdata):
    for i in re.findall(metadata_regex_xml, imgdata):
        metadata_xml.append(i)


#PRINT ORDINARY DATA
for i in metadata_ord:
    print(i)

#print(metadata_xml)

xml_meta_touples = xml_meta_handler.handle_xml_meta(metadata_xml)

#
# for key, value in xml_meta_touples.items():
#     if value is not "0" and key is not "WebStatement":
#        print(key, " ", value)





