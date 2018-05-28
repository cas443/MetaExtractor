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


master = Tk()
master.title("MetaEx: Image Metadata Extraction Tool")
master.configure(background="#a5d6a7")
master.pack_propagate(0)
master.geometry('1120x600')

#----LEFT----
left = Frame(master, width=200, height=500, highlightthickness=0, bg="#a5d6a7")
left.grid(row=0, column=0, padx=10, pady=2, sticky=N+S)

logo = Label(left, text="MetaEx", fg="#00695C", bg="#a5d6a7", font="Verdana 30 bold", underline=True)
logo.grid(row=0, column=0, padx=10, pady=30)

image = Image.open(location)
image = image.resize((300,250), Image.ANTIALIAS)
imageEx = ImageTk.PhotoImage(image, master=master)
Label(left, image=imageEx).grid(row=1, column=0, padx=10, pady=15)

Label(left, text="Other Information", font="Verdana 11 bold", fg="#00695C", bg="#a5d6a7", pady=10).grid(row=2, column=0)

extra_information = "Filename: " + filename + "\n" + "Path: " + location
info = Label(left, text=extra_information, font="Verdana 10 bold", bg="#a5d6a7", fg="#00897B")
info.grid(row=3, column=0)

#----MIDDLE----
separator = ttk.Separator(master, orient="vertical")
separator.grid(row=0, column=1, sticky="sn", rowspan=1)

#----RIGHT----
right = Frame(master,  bg="#a5d6a7", highlightthickness=0, highlightbackground="#a5d6a7", width=500, height=500)
right.grid(row=0, column=2, padx=10, pady=2, sticky="ns")

intro = Label(right, text="Image Metadata", fg="#d7ffd9", bg="#75a478", font="Verdana 10 bold", height=2, width=70)
intro.grid(row=0, column=0, padx=10, pady=20)

table = Frame(right,  bg="#a5d6a7", highlightthickness=0, highlightbackground="#a5d6a7", width=500, height=500)
table.grid(row=1, column=0, padx=10, pady=2, sticky="ns")

canvas = Canvas(table, width=600, height=440, background="#a5d6a7", highlightbackground="#a5d6a7")
scrolly = Scrollbar(table, orient='vertical', command=canvas.yview)

i = 0
for key, value in metadata_xml.items():
    myText = key + ": " + value
    label = Label(canvas, text=myText)
    canvas.create_window(0, i * 50, anchor='nw', window=label, height=15)
    canvas.configure(background="#ff34ff")
    i += 1

# # display labels in the canvas
# for i in range(10):
#     label = Label(canvas, text='label %i' % i)
#     canvas.create_window(0, i*30, anchor='nw', window=label, height=15)
#     canvas.configure(background="#ff34ff")

canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrolly.set, background="#a5d6a7")
#canvas.config(width=600, height=440)
canvas.pack(fill='both', expand=True, side='left')
scrolly.pack(fill='y', side='right')

master.mainloop()




