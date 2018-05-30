import xml_meta_handler, ord_meta_handler
import gui_handler

import re
from tkinter import *
import tkinter.ttk as ttk
from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
from tkinter import filedialog


def start(location, meta_XML, meta_ODR):
    file = open(location, "rb")
    imgdata = file.read()
    file.close()

    imgdata = str(imgdata)

    # print(imgdata[:50000])

    filename = re.search(r"(?:.*/)(.*)(?=)", location).group(1)
    print("[+] METADATA FROM FILE: ", filename)

    #default values in cse they are False
    metadata_ord = []
    metadata_xml = {"" : ""}
    if meta_XML:
        metadata_ord = ord_meta_handler.handle_meta(imgdata)
    if meta_ODR:
        metadata_xml = xml_meta_handler.handle_meta(imgdata)

    print(type(metadata_ord), type(metadata_xml))

    all_meta = ""

    # PRINT XML METADATA
    for key, value in metadata_xml.items():
        if value is not "0" and key is not "WebStatement":
            item = key + ":\t " + value + "\n"
            all_meta += item

    # PRINT ORDINARY METADATA
    for i in metadata_ord:
        item = i + "\n"
        all_meta += item

    ###########################################################################################
    #                                       GUI
    ###########################################################################################

    gui_handler.gui(metadata_ord, metadata_xml, location, filename)


if __name__ == "__main__":
    #location = askopenfilename(title="Select image for metadata extraction", filetypes=[("Image Files", "*.jpg"), ("Image Files", "*.png")] )


    #location = "/home/jo/Desktop/MetaImages/basic_maths.jpg"
    location = "/home/jo/Desktop/MetaImages/pasta_cooked.jpg"

    start(location, True, True)




