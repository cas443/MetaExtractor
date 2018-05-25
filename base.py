import xml_meta_handler, ord_meta_handler
import re
from tkinter import *
import tkinter.ttk as ttk
from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


#location = askopenfilename(title="Select image for metadata extraction", filetypes=[("Image Files", "*.jpg"), ("Image Files", "*.png")] )
#
# if ".jpg" not in location or ".JPG" not in location:
#     messagebox.showerror("Error", "Invalid file chosen.")


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

#PRINT XML METADATA
for key, value in metadata_xml.items():
    if value is not "0" and key is not "WebStatement":
        item = key + ":\t " + value + "\n"
        all_meta += item

#PRINT ORDINARY METADATA
for i in metadata_ord:
    item = i + "\n"
    all_meta += item


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

text1 = Text(right, height=30, width=80)
scroll = Scrollbar(right, command=text1.yview)
text1.config(yscrollcommand=scroll.set)
text1.insert(END, all_meta)
text1.pack(side=LEFT, fill=Y)
scroll.config(command=text1.yview)
scroll.pack(side=RIGHT, fill=Y)


master.mainloop()




