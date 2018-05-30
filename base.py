import xml_meta_handler, ord_meta_handler, gui_handler
import re
from tkinter import *
import tkinter.ttk as ttk
from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
from tkinter import filedialog




#location = askopenfilename(title="Select image for metadata extraction", filetypes=[("Image Files", "*.jpg"), ("Image Files", "*.png")] )
#
# if ".jpg" not in location or ".JPG" not in location:
#     messagebox.showerror("Error", "Invalid file chosen.")


#location = "/home/jo/Desktop/MetaImages/basic_maths.jpg"
location = "/home/jo/Desktop/MetaImages/pasta_cooked.jpg"
#location = "/home/jo/Desktop/MetaImages/image.jpg"
#location = "/home/jo/Desktop/MetaImages/villa1.JPG"
#location = "/home/jo/Desktop/MetaImages/510222832.jpg"
#location = "/home/jo/Desktop/MetaImages/Apple iPhone 4S.jpg"

#location = "/home/jo/Pictures/IMG_20170617_161233.jpg"

file = open(location, "rb")
imgdata = file.read()
file.close()

imgdata = str(imgdata)

#print(imgdata[:50000])

filename = re.search(r"(?:.*/)(.*)(?=)", location).group(1)
print("[+] METADATA FROM FILE: ", filename)

metadata_ord = ord_meta_handler.handle_meta(imgdata)
metadata_xml = xml_meta_handler.handle_meta(imgdata)

print(type(metadata_ord), type(metadata_xml))

all_meta = ""

#PRINT XML METADATA
for key, value in metadata_xml.items():
    if value is not "0" and key is not "WebStatement":
        item = key + ":\t " + value + "\n"
        all_meta += item

#PRINT ORDINARY METADATA
for i in metadata_ord:
    item = i + "\n"
    all_meta += item


###########################################################################################
#                                       GUI
###########################################################################################

gui_handler.gui(metadata_ord, metadata_xml, location, filename)


