import meta_handler
import gui_handler, scraper
import compare_handler

import re, os
from tkinter import *
import tkinter.ttk as ttk
from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
from tkinter import filedialog


def start(location):
    try:
        file = open(location, "rb")
        imgdata = file.read()
        file.close()

        imgdata = str(imgdata)

        filename = re.search(r"(?:.*/)(.*)(?=)", location).group(1)
        print("[+] READING METADATA FROM: ", filename)

        metadata_xml, metadata_ord = meta_handler.handle_meta(imgdata)

        # GUI
        gui_handler.gui(metadata_ord, metadata_xml, location, filename)

    except:
       print("[-] No valid file given. No worries.")


def goto_start():
    location = askopenfilename(initialdir="/home/jo/Desktop", title="Select image for metadata extraction", filetypes=[("Image Files", "*.jpg"), ("Image Files", "*.png")] )
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

    b3 = Button(mainframe, text="Compare Metadata of 2 images", command=compare_handler.compare_meta)
    b3.grid(row=3, column=0, padx=100, pady=10)

    b4 = Button(mainframe, text="Exit", command=master.quit)
    b4.grid(row=4, column=0, padx=100, pady=10)

    footer = Frame(master, width=200, height=50, highlightthickness=0, bg="#fff3ff")
    footer.grid(row=1, column=0, padx=10, pady=2, sticky=N + S)

    censor = Label(footer, text="A summer project", fg="#00695C", bg="#ffffff", font="Verdana 8", underline=False)
    censor.grid(row=1, column=0, padx=100, pady=0, sticky=S)

    master.mainloop()







