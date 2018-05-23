import xml_meta_handler, ord_meta_handler
import re
from tkinter.filedialog import askopenfilename
from tkinter import *

#location = askopenfilename()

#location = "/home/jo/Desktop/basic_maths.jpg"
location = "/home/jo/Desktop/pasta_cooked.jpg"
#location = "/home/jo/Desktop/image.jpg"
#location = "/home/jo/Desktop/villa1.JPG"
#location = "/home/jo/Desktop/510222832.jpg"

file = open(location, "rb")
imgdata = file.read()
file.close()

imgdata = str(imgdata)

#print(imgdata[:50000])

print("[+] METADATA FROM FILE: ", re.search(r"(?:.*/)(.*)(?=)", location).group(1))

metadata_ord = ord_meta_handler.handle_meta(imgdata)
metadata_xml = xml_meta_handler.handle_meta(imgdata)

print(type(metadata_ord), type(metadata_xml))

all_meta = ""



#PRINT XML METADATA
for key, value in metadata_xml.items():
    if value is not "0" and key is not "WebStatement":
        all_meta += key + ":\t " + value + "\n"
        #print(key, " ", value)

#PRINT ORDINARY METADATA
for i in metadata_ord:
    all_meta += i + "\n"
    #print(i)

#print(all_meta)

master = Tk()
scroll = Scrollbar(master)
text = Text(master, height=30, width=80)
scroll.pack(side=RIGHT, fill=Y)
text.pack(side=LEFT, fill=Y)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
text.insert(END, all_meta)
# label = Label(master, text=all_meta,)
# label.pack()
mainloop()




