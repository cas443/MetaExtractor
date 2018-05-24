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
    xml_counter = 0
    #PRINT XML METADATA
    for key, value in metadata_xml.items():
        if value is not "0" and key is not "WebStatement":
            item = key + ":\t " + value + "\n"
            row = xml_counter
            #Label(frame, text=item,  width=3, borderwidth="1", relief="solid").grid(row=row, column=0)
            Label(frame, text=item).grid(row=row, column=0, sticky="w")
            xml_counter += 1

    #PRINT ORDINARY METADATA
    for i in metadata_ord:
        item = i + "\n"
        row = metadata_ord.index(i)
        #Label(frame, text=item, width=3, borderwidth="1", relief="solid").grid(row=row, column=0)
        Label(frame, text=item).grid(row=row, column=0, sticky="w")


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
right = Frame(master, width=400, height = 700, bg="white", highlightthickness=0, highlightbackground="white")
right.grid(row=0, column=1, padx=10, pady=2, sticky=N+S)

canvas = Canvas(right, borderwidth=0, background="#ffffff")
innerRight = Frame(canvas, background="#ffffff")
vsb = Scrollbar(right, orient="vertical", command=canvas.yview) #attached to right, not inner right !
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=innerRight, anchor="nw")

populate(innerRight)
#Label(innerRight, text=all_meta).grid(row=0, column=0)


# text1 = Listbox(right, height=30, width=80, text=all_meta, bg="white")
# text1.grid(row=1, column=1, padx=10, pady=10)
# scroll = Scrollbar(right, orient='verical', command=text1.y)
# text1.config(yscrollcommand=scroll.set)
# scroll.grid(row=2, sticky="ew")
# text1.pack(side=LEFT, fill=Y)


# text1 = Label(right, height=30, width=80, text=all_meta, bg="white")
# text1.grid(row=1, column=1, padx=10, pady=10)
# scroll = Scrollbar(right, orient='verical', command=text1.y)
# text1.config(yscrollcommand=scroll.set)
# scroll.grid(row=2, sticky="ew")
# #text1.config(yscrollcommand=scroll.set)
# #text1.insert(END, all_meta)
# text1.pack(side=LEFT, fill=Y)




#scroll.config(command=text1.yview)
#scroll.pack(side=RIGHT, fill=Y)

# circleCanvas = Canvas(right, width=100, height=100, bg='white', highlightthickness=1, highlightbackground="#333")
# circleCanvas.grid(row=0, column=0, padx=10, pady=2)
#
# btnFrame = Frame(right, width=200, height = 200, bg="#C8F9C4")
# btnFrame.grid(row=1, column=0, padx=10, pady=2)
#
# colorLog = Text(right, width = 30, height = 10, takefocus=0, highlightthickness=1, highlightbackground="#333")
# colorLog.grid(row=2, column=0, padx=10, pady=2)
#
# redBtn = Button(btnFrame, text="Red", bg="#EC6E6E")
# redBtn.grid(row=0, column=0, padx=10, pady=2)
#
# yellowBtn = Button(btnFrame, text="Yellow", bg="#ECE86E")
# yellowBtn.grid(row=0, column=1, padx=10, pady=2)
#
# greenBtn = Button(btnFrame, text="Green", bg="#6EEC77")
# greenBtn.grid(row=0, column=2, padx=10, pady=2)

# master.title("MetaExtractor")
# s = ttk.Style()
# print(s.theme_names())
# s.theme_use("clam")
#
# text0 = Text(master, height=30, width=50)
# text1 = Text(master, height=30, width=80)
# scroll = Scrollbar(master, command=text1.yview)
# image = Image.open(location)
# image = image.resize((300,250), Image.ANTIALIAS)
# i = ImageTk.PhotoImage(image, master=master)
#
# text0.insert(END, "\n")
# text0.image_create(END, image=i)
# text0.pack(side=LEFT)
#
# text1.config(yscrollcommand=scroll.set)
# text1.insert(END, all_meta)
# text1.pack(side=LEFT, fill=Y)
#
# scroll.config(command=text1.yview)
# scroll.pack(side=RIGHT, fill=Y)




mainloop()




