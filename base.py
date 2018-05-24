import xml_meta_handler, ord_meta_handler
import re
from tkinter import *
import tkinter.ttk as ttk
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


#location = askopenfilename(title="Select image for metadata extraction", filetypes=[("Image Files", "*.jpg")])

#location = "/home/jo/Desktop/basic_maths.jpg"
location = "/home/jo/Desktop/pasta_cooked.jpg"
#location = "/home/jo/Desktop/image.jpg"
#location = "/home/jo/Desktop/villa1.JPG"
#location = "/home/jo/Desktop/510222832.jpg"
#location = "/home/jo/Desktop/Apple iPhone 4S.jpg"

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


def populate(frame):
    item = ""
    row = 0
    #PRINT XML METADATA
    for key, value in metadata_xml.items():
        if value is not "0" and key is not "WebStatement":
            item = key + ":\t " + value + "\n"
            #Label(frame, text=item,  width=3, borderwidth="1", relief="solid").grid(row=row, column=0)
            Label(frame, text=item).grid(row=row, column=0, sticky="w")
            row += 1

    #PRINT ORDINARY METADATA
    for i in metadata_ord:
        item = i + "\n"
        #Label(frame, text=item, width=3, borderwidth="1", relief="solid").grid(row=row, column=0)
        Label(frame, text=item).grid(row=row, column=0, sticky="w")
        row += 1


master = Tk()
master.configure(background="white")

#Left Frame and its contents
left = Frame(master, width=200, height=700, highlightthickness=0, bg="white")
left.grid(row=0, column=0, padx=10, pady=2, sticky=N+S)

logo = Image.open("/home/jo/Desktop/metaex.png")
logoEx = ImageTk.PhotoImage(logo, master=master)
Label(left, image=logoEx).grid(row=0, column=0, padx=10, pady=30)

image = Image.open(location)
image = image.resize((300,250), Image.ANTIALIAS)
imageEx = ImageTk.PhotoImage(image, master=master)
Label(left, image=imageEx).grid(row=2, column=0, padx=10, pady=15)

#Right Frame and its contents
right = Frame(master,  bg="white", highlightthickness=0, highlightbackground="white")
right.grid(row=0, column=1, padx=10, pady=2, sticky=N+S)

canvas = Canvas(right, borderwidth=0, background="#ffffff")
innerRight = Frame(canvas, background="#ffffff")
vsb = Scrollbar(right, orient="vertical", command=canvas.yview) #attached to right, not inner right !
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.create_window((4,4), window=innerRight, anchor="nw", height=700, width=800)
canvas.pack(side="left", fill="both", expand=True)

populate(innerRight)



master.mainloop()




