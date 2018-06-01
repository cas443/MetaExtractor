from PIL import Image, ImageTk
from tkinter import *
import ord_meta_handler, xml_meta_handler, gui_handler, scrape_handler
import subprocess

from tkinter import *
import tkinter.ttk as ttk
from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
from tkinter import filedialog

class _PopuleteGui():

    i=0

    def __init__(self, master, location, metadata_xml, metadata_ord):
        self.master = master
        self.location = location
        self.metadata_xml = metadata_xml
        self.metadata_ord = metadata_ord
        self.textToSave = []
        self.a1 = False
        self.a2 = False

        self.spider = scrape_handler.Spider
        print()

    def _pop_image_(self):
        image = Image.open(self.location)
        image = image.resize((300, 250), Image.ANTIALIAS)
        imageEx = ImageTk.PhotoImage(image, master=self.master)

        return imageEx

    def _pop_about_(self):
        ABOUT_TEXT = """

            About


            This tool has been created as a summer project. Its intended 
            purpose is to educate as to what type of information is 
            stored ithin image files.

            This software comes with no guarantee. Use at your own risk.    
            """

        top = Toplevel()
        label = Label(top, text=ABOUT_TEXT, heigh=0, width=60)
        label.configure(background="#ffffff")
        label.pack()

    def _pop_usage_(self):
        USAGE_TEXT = """

            How to use


            Go to File->Open New... and choose the image you want to extract 
            metadata for.

            The data should appear in the "Image Metadata" box in the main 
            window.

            To save the metadata go to File->Save Meta to file... and choose 
            the location and the name you would like to save the data under.

            Under the Filter tab you can choose which type of metadata to display. 

            """
        top = Toplevel()
        label = Label(top, text=USAGE_TEXT, heigh=0, width=65)
        label.configure(background="#ffffff")
        label.pack()

    def _pop_xml_(self, canvas):
        temp = ""
        for key, value in self.metadata_xml.items():
            if "0" not in value and "http" not in value:
                l = len(key)
                tab = ""
                if l < 9:
                    tab = "\t\t\t"
                elif l < 20:
                    tab = "\t\t"
                elif l < 30:
                    tab = "\t"
                else:
                    tab = ""

                myText = key + ": " + tab + value
                label = Label(canvas, text=myText)
                canvas.create_window(0, self.i * 22, anchor='nw', window=label, height=15)
                label.configure(background="#ffffff")
                temp += myText + "\n"
                self.i += 1

        self.textToSave.append(temp)
        self.a1 = True
        return  self.textToSave

    def _pop_ord_(self, canvas):
        temp = ""
        for j in self.metadata_ord:
            label = Label(canvas, text=j)
            canvas.create_window(0, self.i * 22, anchor='nw', window=label, height=15)
            label.configure(background="#ffffff")
            temp += j + "\n"
            self.i += 1

        self.textToSave.append(temp)
        self.a2= True
        return  self.textToSave

    def _save_meta_(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt", initialfile='METAEX_metadata.txt', )
        text = ""
        for i in self.textToSave:
            text += i
        f.write(text)
        f.close()

    def _open_new_(self):
        location = askopenfilename(title="Select image for metadata extraction", filetypes=[("Image Files", "*.jpg"), ("Image Files", "*.png")])

        file = open(location, "rb")
        imgdata = file.read()
        file.close()

        imgdata = str(imgdata)

        filename = re.search(r"(?:.*/)(.*)(?=)", location).group(1)
        print("[+] METADATA FROM FILE: ", filename)

        metadata_ord = ord_meta_handler.handle_meta(imgdata)
        metadata_xml = xml_meta_handler.handle_meta(imgdata)

        gui_handler._GUI(metadata_ord, metadata_xml, location, filename)

    def _filter_(self, XML_bool, ORD_bool):

        print()

        if (self.a1 is True and self.a2 is True) or (self.a1 is True and self.a2 is False) or (self.a1 is False and self.a2 is True):
            if self.metadata_xml and XML_bool:
                self.textToSave = self.textToSave[0]
                self.master.update_idletasks()
            if self.metadata_xml and self.metadata_ord and ORD_bool:
                self.textToSave = self.textToSave[1]
                print(self.textToSave)
                self.master.update_idletasks()
            if not self.metadata_xml and self.metadata_ord and ORD_bool:
                self.textToSave = self.textToSave[0]
                print(self.textToSave)
                self.master.update_idletasks()
            if XML_bool and ORD_bool:
                self.textToSave = self.textToSave
                self.master.update_idletasks()

    def _url_scrap_(self):
        url = ""

        master = Tk()
        Label(master, text="Scrap URL: ").grid(row=0)

        e1 = Entry(master)
        e1.grid(row=0, column=1)

        b = Button(master, text='Scrape', command=subprocess.call("scrapy crawl spidyBoo"))
        b.configure(bg="#1ba1e2", fg="#ffffff")
        b.grid(row=3, column=0, sticky=W, pady=4, padx=3)
