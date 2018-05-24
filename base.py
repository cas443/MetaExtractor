import xml_meta_handler, ord_meta_handler
import re
from tkinter import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


location = askopenfilename(title="Select image for metadata extraction", filetypes=[("Image Files", "*.jpg")])

#location = "/home/jo/Desktop/basic_maths.jpg"
#location = "/home/jo/Desktop/pasta_cooked.jpg"
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
        all_meta += key + ":\t " + value + "\n"
        #print(key, " ", value)

#PRINT ORDINARY METADATA
for i in metadata_ord:
    all_meta += i + "\n"
    #print(i)


master = Tk()
master.title("MetaExtractor")

text0 = Text(master, height=30, width=50)
text1 = Text(master, height=30, width=80)
scroll = Scrollbar(master, command=text1.yview)
image = Image.open(location)
image = image.resize((300,250), Image.ANTIALIAS)
i = ImageTk.PhotoImage(image, master=master)

text0.insert(END, "\n")
text0.image_create(END, image=i)
text0.pack(side=LEFT)

text1.config(yscrollcommand=scroll.set)
text1.insert(END, all_meta)
text1.pack(side=LEFT, fill=Y)

scroll.config(command=text1.yview)
scroll.pack(side=RIGHT, fill=Y)




mainloop()




