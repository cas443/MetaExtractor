import base
from tkinter import *
import tkinter.ttk as ttk
from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
from tkinter import filedialog

textToSave = ""


def openFile():

    location = askopenfilename(title="Select image for metadata extraction", filetypes=[("Image Files", "*.jpg"), ("Image Files", "*.png")])

    base.start(location)

def saveFile():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt", initialfile='METAEX_metadata.txt',)
    f.write(textToSave)
    f.close()

def crawl():
    global filter_xml
    global filter_ord

    filter_xml = True
    filter_ord = True


def hello():
    print("hello")

def about():
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

def usage():
    USAGE_TEXT = """

    How to use


    Go to File->Open New... and choose the image you want to extract 
    metadata for.

    The data should appear in the "Image Metadata" box in the main 
    window.

    To save the metadata go to File->Save Meta to file... and choose 
    the location and the name you would like to save the data under.

    """
    top = Toplevel()
    label = Label(top, text=USAGE_TEXT, heigh=0, width=65)
    label.configure(background="#ffffff")
    label.pack()

def terminology():
    TEXT_WHAT_IT_IS = """
    
                Metadata:
                
                Data that is stored within an image that is the image itself.
                An example would be Exif data which would contain the date and 
                the timestamp of when the image was taken. Other data such as 
                camera make and model, geolocation, how the image was edited as
                well as different tags, copyrights or creators can also be seen
                although their occurance is rarer.
                
                

                Image Histogram:

                An image histogram is a graphical representation of the tonal 
                distribution in a digital image, It plots the number of pixels 
                for each tonal value.

                Through the use of image histograms, the viewer can judge the 
                entire tonal destribution at a glance.

            """

    top = Toplevel()
    label = Label(top, text=TEXT_WHAT_IT_IS, heigh=0, width=65)
    label.configure(background="#ffffff")


    label.pack()


def gui(metadata_ord, metadata_xml, location, filename):

    global textToSave

    CMAIN = "#ffffff"  #a5d6a7"
    CDARKER = "#024016" # #1ba1e2
    CLOGO="#00695C"



    master = Tk()
    master.title("MetaEx: Image Metadata Extraction Tool")
    master.configure(background=CMAIN)
    master.pack_propagate(0)
    master.geometry('1120x540')

    # ----MENU----
    menubar = Menu(master)
    menubar.configure(background="#ffffff")

    # create a pulldown menu, and add it to the menu bar
    filemenu = Menu(menubar, tearoff=0)
    filemenu.configure(background="#ffffff")
    filemenu.add_command(label="Open New...", command=openFile)
    filemenu.add_command(label="Save Meta to file...", command=saveFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=master.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    # create more pulldown menus
    editmenu = Menu(menubar, tearoff=0)
    editmenu.configure(background="#ffffff")
    editmenu.add_command(label="URL", command=crawl)
    menubar.add_cascade(label="Crawl", menu=editmenu)

    displaymenu = Menu(menubar, tearoff=0)
    displaymenu.configure(background="#ffffff")
    displaymenu.add_command(label="Image RGB Histogram", command=usage)
    menubar.add_cascade(label="Display", menu=displaymenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.configure(background="#ffffff")
    helpmenu.add_command(label="About", command=about)
    helpmenu.add_command(label="How to use", command=usage)
    helpmenu.add_command(label="Terminology", command=terminology)
    menubar.add_cascade(label="Help", menu=helpmenu)

    # display the menu
    master.config(menu=menubar)

    # ----LEFT----
    left = Frame(master, width=200, height=500, highlightthickness=0, bg=CMAIN)
    left.grid(row=0, column=0, padx=10, pady=2, sticky=N + S)

    logo = Label(left, text="MetaEx", fg=CLOGO, bg=CMAIN, font="Verdana 30 bold", underline=True)
    logo.grid(row=0, column=0, padx=10, pady=30)

    image = Image.open(location)
    image = image.resize((300, 250), Image.ANTIALIAS)
    imageEx = ImageTk.PhotoImage(image, master=master)
    Label(left, image=imageEx).grid(row=1, column=0, padx=10, pady=15)

    Label(left, text="Other Information", font="Verdana 11 bold", fg="#00695C", bg=CMAIN, pady=10).grid(row=2, column=0, sticky="nw")

    extra_information = "Filename: " + filename
    info = Label(left, text=extra_information, font="Verdana 10 ", bg=CMAIN, fg="#00897B")
    info.grid(row=3, column=0, sticky="nw")

    extra_information2 = "Path: " + location
    info2 = Label(left, text=extra_information2, font="Verdana 10 ", bg=CMAIN, fg="#00897B")
    info2.grid(row=4, column=0, sticky="nw")

    # ----MIDDLE----
    # separator = ttk.Separator(master, orient="vertical")
    # separator.grid(row=0, column=1, sticky="sn", rowspan=2)

    # ----RIGHT----
    right = Frame(master, bg=CMAIN, highlightthickness=0, highlightbackground=CMAIN, width=500, height=500)
    right.grid(row=0, column=2, padx=50, pady=2, sticky="ns")

    intro = Label(right, text="Image Metadata", fg="#ffffff", bg="#1ba1e2", font="Verdana 10 bold", height=2, width=70)
    intro.grid(row=0, column=0, padx=10, pady=20)



    table = Frame(right, bg=CMAIN, highlightthickness=0, highlightbackground=CMAIN, width=500, height=400)
    table.grid(row=1, column=0, padx=10, pady=0, sticky="ns")

    canvas = Canvas(table, width=600, height=440, background=CMAIN, highlightbackground=CMAIN)
    scrolly = Scrollbar(table, orient='vertical', command=canvas.yview)

    i = 0
    for key, value in metadata_xml.items():
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
            canvas.create_window(0, i * 22, anchor='nw', window=label, height=15)
            label.configure(background=CMAIN)
            textToSave += myText + "\n"
            i += 1

    for j in metadata_ord:
        label = Label(canvas, text=j)
        canvas.create_window(0, i * 22, anchor='nw', window=label, height=15)
        label.configure(background=CMAIN)
        textToSave += j + "\n"
        i += 1

    canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrolly.set, background=CMAIN)
    # canvas.config(width=600, height=440)
    canvas.pack(fill='both', expand=True, side='left')
    scrolly.configure(bg="#ffffff")
    scrolly.pack(fill='y', side='right')

    master.mainloop()
