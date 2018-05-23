import xml_meta_handler, ord_meta_handler
import re
from tkinter import *
from PIL import Image, ImageTk

#location = askopenfilename()

#location = "/home/jo/Desktop/basic_maths.jpg"
#location = "/home/jo/Desktop/pasta_cooked.jpg"
#location = "/home/jo/Desktop/image.jpg"
location = "/home/jo/Desktop/villa1.JPG"
#location = "/home/jo/Desktop/510222832.jpg"

file = open(location, "rb")
imgdata = file.read()
file.close()

imgdata = str(imgdata)

#print(imgdata[:50000])

filename = re.search(r"(?:.*/)(.*)(?=)", imgdata).group(1)
print("[+] METADATA FROM FILE: ", filename, location)

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


master = Tk()
text0 = Text(master, height=30, width=50)
text1 = Text(master, height=30, width=80)
scroll = Scrollbar(master, command=text1.yview)
image = Image.open(location)
image = image.resize((300,250), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)



text0.insert(END, "\n")
text0.image_create(END, image=image)
text0.pack(side=LEFT)

text1.pack(side=LEFT, fill=Y)
text1.config(yscrollcommand=scroll.set)
text1.insert(END, all_meta)

scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=text1.yview)





mainloop()




