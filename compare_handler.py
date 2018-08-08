from tkinter.filedialog import askopenfilename
import tkinter
from tkinter import *
import meta_handler
import re



def compare_meta():
    image1 = askopenfilename(initialdir="/home/jo/Desktop", title="Select image for metadata extraction", filetypes=[("Image Files", "*.jpg"), ("Image Files", "*.png")] )
    image2 = askopenfilename(initialdir="/home/jo/Desktop", title="Select image for metadata extraction", filetypes=[("Image Files", "*.jpg"), ("Image Files", "*.png")] )

    try:
        file1 = open(image1, "rb")
        file2 = open(image2, "rb")

        imgdata1 = file1.read()
        imgdata2 = file2.read()

        file1.close()
        file2.close()

        imgdata1 = str(imgdata1)
        imgdata2 = str(imgdata2)

    except:
        print("[ERR] An error has occured when reading in compare images.")
        pass

    filename1 = re.search(r"(?:.*/)(.*)(?=)", imgdata1).group(1)
    filename2 = re.search(r"(?:.*/)(.*)(?=)", imgdata2).group(1)
    print("[+] COMPARING IMAGES AT: {} AND {}".format(image1, image2))

    metadata_xml1, metadata_ord1 = meta_handler.handle_meta(imgdata1)
    metadata_xml2, metadata_ord2 = meta_handler.handle_meta(imgdata2)

    if len(metadata_xml1) > len(metadata_xml2):
        lmeta = len(metadata_xml2)
    else: lmeta = len(metadata_xml1)

    print("\n[+] Metadata that is the same in both files: \n")

    commonMeta = ""

    for i in range(lmeta):
        if list(metadata_xml1.keys())[i] == list(metadata_xml2.keys())[i] or list(metadata_xml1.values())[i] == list(metadata_xml2.values())[i] :
            print("\t" + list(metadata_xml1.keys())[i] + ": " + list(metadata_xml2.values())[i])
            commonMeta += list(metadata_xml1.keys())[i] + ": " + list(metadata_xml2.values())[i] + "\n"

    print("\n")
    for i in range(len(metadata_ord1)):
        if metadata_ord1[i]== metadata_ord2[i]:
            print("\t" + metadata_ord1[i])
            commonMeta += metadata_ord1[i] + "\n"


    tk = tkinter.Tk()

    frame1 = tkinter.Frame(master=tk)
    frame1.grid(row=0, column=0)

    lable1 = tkinter.Label(frame1, text="Common Metadata between the 2 chosen files", bg="#ffffff")
    lable1.grid(row=0, column=0)

    textbox1 = tkinter.Text(frame1, bg="#ffffff", height=35, width=110)
    textbox1.insert(INSERT, commonMeta)
    textbox1.grid(row=1, column=0)



    tk.mainloop()


