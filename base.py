import xml_meta_handler, ord_meta_handler
import gui_handler

import re, os
from tkinter import *
import tkinter.ttk as ttk
from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
from tkinter import filedialog


def start(location):
    file = open(location, "rb")
    imgdata = file.read()
    file.close()

    imgdata = str(imgdata)

    # print(imgdata[:50000])

    filename = re.search(r"(?:.*/)(.*)(?=)", location).group(1)
    print("[+] READING METADATA FROM: ", filename)

    #default values in case they are False
    metadata_ord = ord_meta_handler.handle_meta(imgdata)
    metadata_xml = xml_meta_handler.handle_meta(imgdata)


    ###########################################################################################
    #                                       GUI
    ###########################################################################################

    gui_handler.gui(metadata_ord, metadata_xml, location, filename)


if __name__ == "__main__":
    Tk().withdraw() #crates and hides a 'root' lvl window so that the annoying gray window wont be seen
    #location = askopenfilename(title="Select image for metadata extraction", filetypes=[("Image Files", "*.jpg"), ("Image Files", "*.png")] )


    location = "/home/jo/Desktop/MetaImages/basic_maths.jpg"
    #location = "/home/jo/Desktop/MetaImages/pasta_cooked.jpg"

    start(location)




