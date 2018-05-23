import xml_meta_handler, ord_meta_handler
import re
import tkinter as tk
from tkinter.filedialog import askopenfilename

location = askopenfilename()

#location = "/home/jo/Desktop/basic_maths.jpg"
#location = "/home/jo/Desktop/pasta_cooked.jpg"
#location = "/home/jo/Desktop/image.jpg"
#location = "/home/jo/Desktop/villa1.JPG"
#location = "/home/jo/Desktop/510222832.jpg"

file = open(location, "rb")
imgdata = file.read()
file.close()

imgdata = str(imgdata)

#print(imgdata[:50000])

print("[+] METADATA FROM FILE: ", re.search(r"(?:.*/)(.*)(?=)", location).group(1))

metadata_ord = ord_meta_handler.handle_meta(imgdata)
metadata_xml = xml_meta_handler.handle_meta(imgdata)


#PRINT ORDINARY METADATA
for i in metadata_ord:
    print(i)

#PRINT XML METADATA
for key, value in metadata_xml.items():
    if value is not "0" and key is not "WebStatement":
        print(key, " ", value)




