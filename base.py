import xml_meta_handler, ord_meta_handler
import gui_handler, scraper

import re, os
from tkinter import *
import tkinter.ttk as ttk
from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
from tkinter import filedialog


def start(location):
    #try:
    file = open(location, "rb")
    imgdata = file.read()
    file.close()

    imgdata = str(imgdata)

    # print(imgdata[:50000])

    filename = re.search(r"(?:.*/)(.*)(?=)", location).group(1)
    print("[+] READING METADATA FROM: ", filename)

    # default values in case they are False
    metadata_ord = ord_meta_handler.handle_meta(imgdata)
    metadata_xml = xml_meta_handler.handle_meta(imgdata)

    # GUI
    gui_handler.gui(metadata_ord, metadata_xml, location, filename)

    #except:
    #    print("[-] No valid file given. No worries.")


def goto_start():
    # Tk().withdraw() #crates and hides a 'root' lvl window so that the annoying gray window wont be seen
    location = askopenfilename(title="Select image for metadata extraction", filetypes=[("Image Files", "*.jpg"), ("Image Files", "*.png")] )

    #location = "/home/jo/Desktop/MetaImages/basic_maths.jpg"
    # location = "/home/jo/Desktop/MetaImages/pasta_cooked.jpg"

    start(location)


if __name__ == "__main__":


    master = Tk()
    master.title("MetaEx: Metadata Extraction Tool")
    master.configure(background="#ffffff" )
    master.pack_propagate(0)
    master.geometry("+{}+{}".format(int(master.winfo_screenwidth()/4 - master.winfo_reqwidth()/4), int(master.winfo_screenheight()/2 - master.winfo_reqheight()/2)))

    mainframe = Frame(master, width=200, height=450, highlightthickness=0, bg="#ffffff")
    mainframe.grid(row=0, column=0, padx=10, pady=2, sticky=N + S)

    logo = Label(mainframe, text="MetaEx", fg="#00695C", bg="#ffffff", font="Verdana 30 bold", underline=True)
    logo.grid(row=0, column=0, padx=100, pady=30)

    b = Button(mainframe, text="Open a New Image", command=goto_start)
    b.grid(row=1, column=0, padx=100, pady=0)

    b2 = Button(mainframe, text="Scrape a Webpage", command=scraper.scrape_url)
    b2.grid(row=2, column=0, padx=100, pady=10)

    b3 = Button(mainframe, text="Exit", command=master.quit)
    b3.grid(row=3, column=0, padx=100, pady=10)

    footer = Frame(master, width=200, height=50, highlightthickness=0, bg="#fff3ff")
    footer.grid(row=1, column=0, padx=10, pady=2, sticky=N + S)

    censor = Label(footer, text="A summer project", fg="#00695C", bg="#ffffff", font="Verdana 8", underline=False)
    censor.grid(row=1, column=0, padx=100, pady=0, sticky=S)

    master.mainloop()







