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


if __name__ == "__main__":
    #location = askopenfilename(title="Select image for metadata extraction", filetypes=[("Image Files", "*.jpg"), ("Image Files", "*.png")] )


    #location = "/home/jo/Desktop/MetaImages/basic_maths.jpg"
    location = "/home/jo/Desktop/MetaImages/pasta_cooked.jpg"

    file = open(location, "rb")
    imgdata = file.read()
    file.close()

    imgdata = str(imgdata)

    filename = re.search(r"(?:.*/)(.*)(?=)", location).group(1)
    print("[+] METADATA FROM FILE: ", filename)

    metadata_ord = ord_meta_handler.handle_meta(imgdata)
    metadata_xml = xml_meta_handler.handle_meta(imgdata)

    gui = gui_handler._GUI(metadata_ord, metadata_xml, location, filename);
    gui._mainGuiInterface()




